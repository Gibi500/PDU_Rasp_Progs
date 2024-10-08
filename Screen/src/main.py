import os
import datetime
import time
from time import sleep
import threading
import py3nextion_lib  as nxlib    # simple python3 library to use nextion device
import nextionApp as nxApp         # initialization of the components of the Nextion display
import RPi.GPIO as GPIO

NUMBER_OF_DEVICES = 8

device_pin_0 = 16
device_pin_1 = 20
device_pin_2 = 21
device_turn_on = 12
device_turn_off = 7
screen_connect = 17

green = 2024
red = 63488

state_device = [True, True, True, True, True, True, True, True]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(device_pin_0, GPIO.OUT)
GPIO.setup(device_pin_1, GPIO.OUT)
GPIO.setup(device_pin_2, GPIO.OUT)
GPIO.setup(device_turn_off, GPIO.OUT)
GPIO.setup(device_turn_on, GPIO.OUT)
GPIO.setup(screen_connect, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def update_device_state(pageID, compID, device_id):
    nxlib.nx_setBackground(ser, pageID, compID, (green if state_device[device_id] else red))
    nxlib.nx_setGlobalVariable(ser, "dev{}".format(device_id), 1 if state_device[device_id] else 0)

def toggle_device(pageID, compID, device_id):
    if device_id < 0 or device_id >= 8:
        print("Invalid device_id")
        return 0

    GPIO.output(device_pin_0, (device_id >> 0) & 0x01)
    GPIO.output(device_pin_1, (device_id >> 1) & 0x01)
    GPIO.output(device_pin_2, (device_id >> 2) & 0x01)

    state_device[device_id] = not state_device[device_id]
    update_device_state(pageID, compID, device_id)
    on_off = device_turn_on if state_device[device_id] else device_turn_off
    
    GPIO.output(on_off, GPIO.LOW)
    sleep(10 / 1000000)                     # 10 microseconds delay
    GPIO.output(on_off, GPIO.HIGH)
    sleep(10 / 1000000)                     # 10 microseconds delay
    GPIO.output(on_off, GPIO.LOW) 

    return 1

def turn_all_devices_off():
    for i in range(0, NUMBER_OF_DEVICES):
        state_device[i] = True
        toggle_device(nxApp.ID_HOME_BUTTON_TOGGLE_DEVICES[i][0], nxApp.ID_HOME_BUTTON_TOGGLE_DEVICES[i][1], i)

def screen_connected_callback(channel):
    print("Screen connected!")
    for i in range(0, NUMBER_OF_DEVICES):
        update_device_state(nxApp.ID_HOME_BUTTON_TOGGLE_DEVICES[i][0], nxApp.ID_HOME_BUTTON_TOGGLE_DEVICES[i][1], i)

# make connection to serial UART to read/write NEXTION
ser = nxlib.ser

nxlib.nx_setsys(ser, 'bauds', nxlib.BAUD)   # set default baud (default baud rate of nextion from fabric is 9600)
nxlib.nx_setsys(ser, 'bkcmd',0)             # sets in NEXTION 'no return error/success codes'
nxlib.nx_setcmd_1par(ser,'page',0)          # sets page 0

EndCom = "\xff\xff\xff"                     # 3 last bits to end serial communication

def detect_touch(e_rd, e_rdw):
    global t_rdw, p
    turn_all_devices_off()
    while True:
        try:
            touch = ser.read_until(EndCom)
            if  hex(touch[0]) == '0x65': 
                pageID_touch = touch[1]
                compID_touch = touch[2]
                event_touch = touch[3]
                print("page= {}, component= {}, event= {}".format(pageID_touch,compID_touch,event_touch))

                for i in range(0, NUMBER_OF_DEVICES):
                    if (pageID_touch, compID_touch) == nxApp.ID_HOME_BUTTON_TOGGLE_DEVICES[i]:
                        toggle_device(pageID_touch, compID_touch, i)
                        break
                    if (pageID_touch, compID_touch) == nxApp.ID_BUTTON_TOGGLE_DEVICES[i]:
                        toggle_device(pageID_touch, compID_touch, i)
                        break
        except:
            pass

e_rd = threading.Event()
e_rdw = threading.Event()

end_rd = threading.Event()
end_rdw = threading.Event()

GPIO.add_event_detect(screen_connect, GPIO.FALLING, callback=screen_connected_callback, bouncetime=100)

# THREAD - DETECT push buttons
t_serialread = threading.Thread(target=detect_touch, name='read serial',args=(e_rd,e_rdw,))
t_serialread.start()
