# Screen code

## Installation

first you need to make sure python is installed on your raspberry pi. You can check this by running the following command in the terminal:

```bash
python3 --version
```

If python is not installed you can install it by running the following command:

```bash
sudo apt install python3
```

After you have installed python you can install the required package to make a virtual environment by running the following command:

```bash
sudo apt install python3-pandas python3-venv python3-rpi.gpio
```

After you have installed the required package you can create a virtual environment by running the following command:

```bash
python3 -m venv ~/user_interface/.venv
```

After you have created the virtual environment you can activate it by running the following command:

```bash
source ~/user_interface/.venv/bin/activate
```

After you have activated the virtual environment you can install the required packages by running the following command:

```bash
# none at the moment
```

After you have installed the required packages you can clone the repository and go to the root of the repository.

Before you can run the code you need to make sure the UART is enabled by running the following command:

```bash
sudo sh ./Screen/shell_scripts/EnableUART.sh
```

If you get a menu you have to disable the serial console by saying no and afterwards it asks to enable the UART you have to say yes.

After you have cloned the repository you can run the code by running the following command:

```bash
python3 ./Screen/src/main.py
```

## Program description

The most important library is the py3nextion_lib.py here are some standerd functions that are used to communicate with the screen. 
There are some general functions. these need a command, the usable commands can be found in the [nextion instruction](https://nextion.tech/instruction-set/) set. Watch out with the commands that are not supported by the screen.
in the code there are some examples of commands you can send but be sure to look on the [website](https://nextion.tech/instruction-set/) of nextion for the right commands.

The program works as follows:
1. The program starts and setups the hardware of the pi.
2. It starts a Thread that listens to the serial port. this tread wil do something else when the screen sends a command. ending with 0xFF 0xFF 0xFF. afterward it looks at the first byte if it is 0x65 it will do what you want. The second byte is the page number and the third byte is the component number. The fourth byte is the event number ?and the fifth and sixth byte are the data?. 
3. My code afterwards looks at witch page and component it is and sends a signal to the MCU to toggle the device. afterwards it will send a command to the screen to toggle the color of the button to show the state of the device.
4. repeat 

### TODO 

- [ ] Try to read the data of the backend using the api to display the data on the screen. 




