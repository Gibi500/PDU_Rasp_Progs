import os
import datetime
import time
from time import sleep
import threading
import py3nextion_lib  as nxlib    # simple python3 library to use nextion device
import nextionApp as nxApp         # initialization of the components of the Nextion display
import RPi.GPIO as GPIO

NUMBER_OF_DEVICES = 5

device_pin_0 = 16
device_pin_1 = 20
device_pin_2 = 21
device_toggle = 12

green = 2024
red = 63488

state_device = [False, False, False, False, False, False, False, False]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(device_pin_0, GPIO.OUT)
GPIO.setup(device_pin_1, GPIO.OUT)
GPIO.setup(device_pin_2, GPIO.OUT)
GPIO.setup(device_toggle, GPIO.OUT)

def toggle_device(pageID, compID, device_id):
    if device_id < 0 or device_id >= 8:
        print("Invalid device_id")
        return 0

    GPIO.output(device_pin_0, (device_id >> 0) & 0x01)
    GPIO.output(device_pin_1, (device_id >> 1) & 0x01)
    GPIO.output(device_pin_2, (device_id >> 2) & 0x01)
    
    GPIO.output(device_toggle, GPIO.LOW)
    sleep(10 / 1000000)                     # 10 microseconds delay
    GPIO.output(device_toggle, GPIO.HIGH)
    sleep(10 / 1000000)                     # 10 microseconds delay
    GPIO.output(device_toggle, GPIO.LOW)

    if state_device[device_id]:
        nxlib.nx_setBackground(ser, pageID, compID, red)
        nxlib.nx_setGlobalVariable(ser, "dev{}".format(device_id), 0)
        state_device[device_id] = False
    else:
        nxlib.nx_setBackground(ser, pageID, compID, green)
        nxlib.nx_setGlobalVariable(ser, "dev{}".format(device_id), 1)
        state_device[device_id] = True
    return 1

    

######### make connection to serial UART to read/write NEXTION
ser = nxlib.ser

nxlib.nx_setsys(ser, 'bauds', nxlib.BAUD)   # set default baud (default baud rate of nextion from fabric is 9600)
nxlib.nx_setsys(ser, 'bkcmd',0)             # sets in NEXTION 'no return error/success codes'
nxlib.nx_setcmd_1par(ser,'page',0)          # sets page 0

EndCom = "\xff\xff\xff"                     # 3 last bits to end serial communication

def detect_touch(e_rd, e_rdw):
    global t_rdw, p
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
                        print("HOME toggle device")
                        break
                    if (pageID_touch, compID_touch) == nxApp.ID_BUTTON_TOGGLE_DEVICES[i]:
                        toggle_device(pageID_touch, compID_touch, i)
                        print("toggle device")
                        break
        except:
            pass

e_rd = threading.Event()
e_rdw = threading.Event()

end_rd = threading.Event()
end_rdw = threading.Event()

# THREAD - DETECT push buttons
t_serialread = threading.Thread(target=detect_touch, name='read serial',args=(e_rd,e_rdw,))
t_serialread.start()
