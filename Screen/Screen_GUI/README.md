# HMI installation for new screens.

## Installation of the script

make sure you have:
- python3
- PySerial

in the previous folder you can find in the readme how to install python3 and the required packages.

```bash
git clone https://github.com/MMMZZZZ/Nexus
```
after you have cloned the repository you can go to the root of the repository.
afterwards you need to change 2 lines of code in the Nexus.py file.

on line 34:
from
```python
        self.ports        = [p.device for p in availablePorts()]
```
to 
```python
        self.ports        = ["/dev/ttyS0"]
```

and on line 239:
from
```python
    ports = [p.device for p in availablePorts()]
```
to
```python
    ports = ["/dev/ttyS0"]
```

then you wil be able to upload the .tft file to the screen.
using the command:

before you need to be sure you are in the right virtual environment.
secondly there are 2 types of displays one old and one new. the new one is the NX4832K035_011C and the old one is the NX4832T035_011C. for those you need different .tft files the new one is the Screen_New_Displays.tft and the old one is Test.tft.

command to upload to the new screen:
```bash
 python3 Nexus/Nexus.py -i ./Screen_New_Displays.tft -p '/dev/ttyS0' -u 512000
```

command to upload to the old screen:
```bash
 python3 Nexus/Nexus.py -i ./Test.tft -p '/dev/ttyS0' -u 512000
```

A visual clue to differentiate the screens is the color of the screen. the new screen has a blue color and the old PCB has a black PCB.

if you upload the wrong file you will get a error on the screen and in the terminal. to resolve this you need to unplug and plugin the screen and try again with the correct file.
