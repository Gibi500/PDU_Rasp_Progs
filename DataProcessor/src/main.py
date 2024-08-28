import signal
import sys
import threading
import time
from time import sleep
from collections import deque
import RPi.GPIO as GPIO
import requests
import json
import concurrent.futures
from enum import Enum

url = "http://localhost:3000/measurements"
myobj = {"device_id": 0, "type_data": 0, "value_data": 0, "delta_time": 0}

data_queue = deque()

device_id = -1

state_acknowledge = False

ACK_MPU = 25
ACK_MCU = 8
DATA0_GPIO = 26
DATA1_GPIO = 19
DATA2_GPIO = 13
DATA3_GPIO = 6
DATA4_GPIO = 5
DATA5_GPIO = 11
DATA6_GPIO = 9
DATA7_GPIO = 10

DATA_GPIOS = [DATA0_GPIO, DATA1_GPIO, DATA2_GPIO, DATA3_GPIO, DATA4_GPIO, DATA5_GPIO, DATA6_GPIO, DATA7_GPIO]

number_of_data_points = 0
device_id = -1
data_type = -1
value_data_final = -1
delta_time = -1

voltage_factor = 1.0 / (2.2 / (4000 + 2.2))     # voltage divider ratio 
current_factor = 1.19 * 30                      # range from 0 to 0.84 so need to remap to 0 to 1 and times 30A
power_active_factor = 250 * 30 * 1.42           # MaxPow is at 0.704 so times 1.42 to remap it to 1 and times 30A and 250V as maximum values
power_imaginary_factor = 250 * 30 * 1.42        # MaxPow is at 0.704 so times 1.42 to remap it to 1 and times 30A and 250V as maximum values
power_apparent_factor = 250 * 30 * 1.42         # MaxPow is at 0.704 so times 1.42 to remap it to 1 and times 30A and 250V as maximum values
power_factor_factor = 1                         # no scaling needed value between -1 and 1
peak_current_factor = 1                         # no clue lost the calculation

class data_commands(Enum):
	VOLTAGE = 0
	CURRENT = 1
	POWER_ACTIVE = 2
	POWER_IMAGINARY = 3
	POWER_APPARENT = 4
	POWER_FACTOR = 5
	PEAK_CURRENT = 6


def data_ready_callback(channel):
    print("DATA_READY_GPIO triggered")
    read_data()

# uint16_t to signed float with e amount of after decimal bits 
def to_float_signed(x,e):
    c = abs((x << 1) >> 1) & 0xFFFF
    sign = 1
    if (x & (1 << (16 - 1))) == 0:
        sign = 1
    elif (x & (1 << (16 - 1))) == 1:
        sign = -1
    f = (1.0 * c) / (2 ** e)
    f = f * sign
    return f

# uint16_t to signed float with e amount of after decimal bits 
def to_float_signed_11_bit(x,e):
    c = abs((x << 1) >> 1) & 0x7FF
    sign = 1
    if (x & (1 << (11 - 1))) == 0:
        sign = 1
    elif (x & (1 << (11 - 1))) == 1:
        sign = -1
    f = (1.0 * c) / (2 ** e)
    f = f * sign
    return f

# uint16_t to unsigned float with e amount of after decimal bits
def to_float_unsigned(x,e):
    c = abs(x) & 0xFFFF
    sign = 1
    f = (1.0 * c) / (2 ** e)
    f = f * sign
    return f

      
def send_data():
    print("send_data started")
    while True:
        if data_queue.__len__() == 0:
            continue
            print("Data queue empty")
        else:
            temp_obj = data_queue.pop()
            print(temp_obj)

            x = requests.post(url, json = temp_obj)
            print(x.text)
            
def read_data():
    data = 0
    for i in range(DATA_GPIOS.__len__()):
        data += (GPIO.input(DATA_GPIOS[i]) << i)
    return data

def acknowledge_read():
    global state_acknowledge
    state_acknowledge = not state_acknowledge
    GPIO.output(ACK_GPIO, state_acknowledge)
    

GPIO.setmode(GPIO.BCM)

GPIO.setup(ACK_MCU, GPIO.OUT)

GPIO.setup(ACK_MPU, GPIO.IN, pull_up_down=GPIO.PUD_UP)

for i in range(DATA_GPIOS.__len__()):
    GPIO.setup(DATA_GPIOS[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)


GPIO.output(ACK_MCU, GPIO.LOW)

pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

print("Main loop")
while True:
    if GPIO.input(ACK_MPU) != state_acknowledge:
        print("read_data started")

        if(device_id == -1):
            print("Device ID not set")
            data = read_data()
            device_id = data & 0x07
            print("Device ID:", device_id)
            data_type = (data >> 3) & 0x07
            print("Data type:", data_type)
            myobj["device_id"] = device_id
            myobj["type_data"] = data_type
            acknowledge_read()
            continue

        if(number_of_data_points == 0):
            print("Number of data points not set")
            number_of_data_points = read_data()
            print("Number of data points:", number_of_data_points)
            acknowledge_read()
            continue

        if(number_of_data_points > 0 and data_type == -1):
            print("Data points left")
            tmp_data = read_data()
            print("Data:", tmp_data)
            match(data_type):
                case data_commands.VOLTAGE.value:
                    value_data_final = to_float_unsigned(tmp_data, 16) * voltage_factor
                    print("Voltage: ", value_data_final)
                case data_commands.CURRENT.value:
                    value_data_final = to_float_signed(tmp_data, 15) * current_factor
                    print("Current: ", value_data_final)
                case data_commands.POWER_ACTIVE.value:
                    value_data_final = to_float_signed(tmp_data, 15) * power_active_factor
                    print("Power active: ", value_data_final) 
                case data_commands.POWER_IMAGINARY.value:
                    value_data_final = to_float_unsigned(tmp_data, 16) * power_imaginary_factor
                    print("Power imaginary: ", value_data_final) 
                case data_commands.POWER_APPARENT.value:
                    value_data_final = to_float_unsigned(tmp_data, 15) * power_apparent_factor
                    print("Power apparent: ", value_data_final)
                case data_commands.POWER_FACTOR.value:
                    tmp_data = tmp_data & 0x7FF
                    value_data_final = to_float_signed_11_bit(tmp_data, 10) * power_factor_factor
                    print("Power factor: ", value_data_final) 
                case data_commands.PEAK_CURRENT.value:
                    value_data_final = to_float(tmp_data, 3) * peak_current_factor # weet nog niet wat er verstuurd word
                    print("Peak current: ", value_data_final) 
                case _:
                    print("Invalid data type")

            myobj["value_data"] = value_data_final
            continue

        if(number_of_data_points > 0 and delta_time == -1):
            print("Delta time not set")
            delta_time = read_data()
            print("Delta time:", delta_time)
            myobj["delta_time"] = delta_time
            acknowledge_read()

            data_queue.append(myobj)
            number_of_data_points -= 1
            # if set of data points is processed reset all values
            if number_of_data_points == 0:
                device_id = -1
                data_type = -1
                value_data_final = -1
                delta_time = -1

        
