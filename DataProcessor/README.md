# Input data code

## Installation

Follow the screen installation guide to install Python3 and the required packages. And use the same virtual environment.

## Program description

The program does a vew things. It reads the data on the 8 data_pins when the ACK_MCU line is different from the ACK_MPU line. The data sequent goes as follows:

|        | 7 (MSB) | 6  | 5  | 4  | 3  | 2     | 1     | 0 (LSB) |
|--------|---------|----|----|----|----|-------|-------|---------|
| Byte 1 | x       | x  | Dt | Dt | Dt | Dev N | Dev N | Dev N   |
| Byte 2 | Dn      | Dn | Dn | Dn | Dn | Dn    | Dn    | Dn      |
| Byte 3 | D       | D  | D  | D  | D  | D     | D     | D       |
| Byte 4 | T       | T  | T  | T  | T  | T     | T     | T       |

Where:
- x: not used
- Dt: data type
- Dev N: Device number
- Dn: number of data points
- D: data
- T: delta time between data points

so the MCU sends first the datatype and the device number. After that, it sends the number of data points, and finally the data, and the delta time between measurements get send "data points" times. 

After it gets the data for one entry (device_id, type_data, value_data, delta_time) it wil make a job to send the data to the database.
