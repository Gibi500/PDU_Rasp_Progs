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
sudo apt install python3-pandas python3-venv
```

After you have installed the required package you can create a virtual environment by running the following command:

```bash
python3 -m venv ~/User_Interface/.venv
```

After you have created the virtual environment you can activate it by running the following command:

```bash
source ~/User_Interface/.venv/bin/activate
```

After you have activated the virtual environment you can install the required packages by running the following command:

```bash
pip install RPi.GPIO
```

After you have installed the required packages you can clone the repository and go to the root of the repository.

Before you can run the code you need to make sure the UART is enabled by running the following command:

```bash
sudo ./Screen/shell_scripts/EnableUART.sh
```

After you have cloned the repository you can run the code by running the following command:

```bash
python3 ./Screen/src/main.py
```

## Program description

The most important library is the py3nextion_lib.py here are some standerd functions that are used to communicate with the screen. 
There are some general functions. these need a command, the usable commands can be found in the [nextion instruction](https://nextion.tech/instruction-set/) set. Watch out with the commands that are not supported by the screen.
in the code there are some examples of commands you can send but be sure to look on the [website](https://nextion.tech/instruction-set/) of nextion for the right commands.