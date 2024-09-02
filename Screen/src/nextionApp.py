#! /usr/bin/python3
# -*- coding: utf-8 -*-
#Ricardos.geral@gmail.com

# set all the components
class NextionApp:

    # initialization of the components used in device

    def __init__(self):
        self.pages = [
            {'id': 0, 'name': 'home',
             'components': [
                 {'id': 6, 'type': 'text', 'name': 't0'},
                 {'id': 7, 'type': 'text', 'name': 't1'},
                 {'id': 8, 'type': 'text', 'name': 't2'},
                 {'id': 9, 'type': 'text', 'name': 't3'},
                 {'id': 10, 'type': 'text', 'name': 't4'},
                 {'id': 12, 'type': 'text', 'name': 't5'},
                 {'id': 14, 'type': 'text', 'name': 't6'},
                 {'id': 16, 'type': 'text', 'name': 't7'}
             ]
             },
            {'id': 1, 'name': 'Device 1',
             'components': [
                 {'id': 2, 'type': 'button', 'name': 'b0'}, # Toggle Button
                 {'id': 3, 'type': 'button', 'name': 'b1'}, # Stats refresh Button
                 {'id': 17, 'type': 'text', 'name': 't13'}, # Voltage
                 {'id': 18, 'type': 'text', 'name': 't14'}, # Current
                 {'id': 19, 'type': 'text', 'name': 't15'}, # Peak Current
                 {'id': 20, 'type': 'text', 'name': 't16'}, # Power factor
                 {'id': 21, 'type': 'text', 'name': 't17'}, # Apparent Power
                 {'id': 22, 'type': 'text', 'name': 't18'}, # Active Power
                 {'id': 23, 'type': 'text', 'name': 't19'} # Imaginary Power
             ]
             },
            {'id': 2, 'name': 'Device 2',
                'components': [
                    {'id': 2, 'type': 'button', 'name': 'b0'}, # Toggle Button
                    {'id': 3, 'type': 'button', 'name': 'b1'}, # Stats refresh Button
                    {'id': 17, 'type': 'text', 'name': 't13'}, # Voltage
                    {'id': 18, 'type': 'text', 'name': 't14'}, # Current
                    {'id': 19, 'type': 'text', 'name': 't15'}, # Peak Current
                    {'id': 20, 'type': 'text', 'name': 't16'}, # Power factor
                    {'id': 21, 'type': 'text', 'name': 't17'}, # Apparent Power
                    {'id': 22, 'type': 'text', 'name': 't18'}, # Active Power
                    {'id': 23, 'type': 'text', 'name': 't19'} # Imaginary Power
             ]
             },
            {'id': 3, 'name': 'Device 3',
                'components': [
                    {'id': 2, 'type': 'button', 'name': 'b0'}, # Toggle Button
                    {'id': 3, 'type': 'button', 'name': 'b1'}, # Stats refresh Button
                    {'id': 17, 'type': 'text', 'name': 't13'}, # Voltage
                    {'id': 18, 'type': 'text', 'name': 't14'}, # Current
                    {'id': 19, 'type': 'text', 'name': 't15'}, # Peak Current
                    {'id': 20, 'type': 'text', 'name': 't16'}, # Power factor
                    {'id': 21, 'type': 'text', 'name': 't17'}, # Apparent Power
                    {'id': 22, 'type': 'text', 'name': 't18'}, # Active Power
                    {'id': 23, 'type': 'text', 'name': 't19'} # Imaginary Power
             ]
             },
            {'id': 4, 'name': 'Device 4',
                'components': [
                    {'id': 2, 'type': 'button', 'name': 'b0'}, # Toggle Button
                    {'id': 3, 'type': 'button', 'name': 'b1'}, # Stats refresh Button
                    {'id': 17, 'type': 'text', 'name': 't13'}, # Voltage
                    {'id': 18, 'type': 'text', 'name': 't14'}, # Current
                    {'id': 19, 'type': 'text', 'name': 't15'}, # Peak Current
                    {'id': 20, 'type': 'text', 'name': 't16'}, # Power factor
                    {'id': 21, 'type': 'text', 'name': 't17'}, # Apparent Power
                    {'id': 22, 'type': 'text', 'name': 't18'}, # Active Power
                    {'id': 23, 'type': 'text', 'name': 't19'} # Imaginary Power
             ]
             },
             {'id': 5, 'name': 'Device 5',
                'components': [
                    {'id': 2, 'type': 'button', 'name': 'b0'}, # Toggle Button
                    {'id': 3, 'type': 'button', 'name': 'b1'}, # Stats refresh Button
                    {'id': 17, 'type': 'text', 'name': 't13'}, # Voltage
                    {'id': 18, 'type': 'text', 'name': 't14'}, # Current
                    {'id': 19, 'type': 'text', 'name': 't15'}, # Peak Current
                    {'id': 20, 'type': 'text', 'name': 't16'}, # Power factor
                    {'id': 21, 'type': 'text', 'name': 't17'}, # Apparent Power
                    {'id': 22, 'type': 'text', 'name': 't18'}, # Active Power
                    {'id': 23, 'type': 'text', 'name': 't19'} # Imaginary Power
             ]
             },
            {'id': 6, 'name': 'Device 6',
                'components': [
                    {'id': 2, 'type': 'button', 'name': 'b0'}, # Toggle Button
                    {'id': 3, 'type': 'button', 'name': 'b1'}, # Stats refresh Button
                    {'id': 17, 'type': 'text', 'name': 't13'}, # Voltage
                    {'id': 18, 'type': 'text', 'name': 't14'}, # Current
                    {'id': 19, 'type': 'text', 'name': 't15'}, # Peak Current
                    {'id': 20, 'type': 'text', 'name': 't16'}, # Power factor
                    {'id': 21, 'type': 'text', 'name': 't17'}, # Apparent Power
                    {'id': 22, 'type': 'text', 'name': 't18'}, # Active Power
                    {'id': 23, 'type': 'text', 'name': 't19'} # Imaginary Power
             ]
             },
            {'id': 7, 'name': 'Device 7',
                'components': [
                    {'id': 2, 'type': 'button', 'name': 'b0'}, # Toggle Button
                    {'id': 3, 'type': 'button', 'name': 'b1'}, # Stats refresh Button
                    {'id': 17, 'type': 'text', 'name': 't13'}, # Voltage
                    {'id': 18, 'type': 'text', 'name': 't14'}, # Current
                    {'id': 19, 'type': 'text', 'name': 't15'}, # Peak Current
                    {'id': 20, 'type': 'text', 'name': 't16'}, # Power factor
                    {'id': 21, 'type': 'text', 'name': 't17'}, # Apparent Power
                    {'id': 22, 'type': 'text', 'name': 't18'}, # Active Power
                    {'id': 23, 'type': 'text', 'name': 't19'} # Imaginary Power
             ]
             },
            {'id': 8, 'name': 'Device 8',
                'components': [
                    {'id': 2, 'type': 'button', 'name': 'b0'}, # Toggle Button
                    {'id': 3, 'type': 'button', 'name': 'b1'}, # Stats refresh Button
                    {'id': 17, 'type': 'text', 'name': 't13'}, # Voltage
                    {'id': 18, 'type': 'text', 'name': 't14'}, # Current
                    {'id': 19, 'type': 'text', 'name': 't15'}, # Peak Current
                    {'id': 20, 'type': 'text', 'name': 't16'}, # Power factor
                    {'id': 21, 'type': 'text', 'name': 't17'}, # Apparent Power
                    {'id': 22, 'type': 'text', 'name': 't18'}, # Active Power
                    {'id': 23, 'type': 'text', 'name': 't19'} # Imaginary Power
                ]
            }



        ]

##  function get page ID and component ID, based on the names of page and component in the class
def get_Ids(pageName, compName):
   for element in NextionApp().pages:
       if element['name'] == pageName:
           pag_id = element['id']
           for component in element['components']:
               if component['name'] == compName:
                   comp_id = component['id']
                   return pag_id, comp_id


# ###INITIAL INPUTS from NEXTION by name
# home page
ID_HOME_BUTTON_TOGGLE_DEVICE1 = get_Ids('home', 't0')
ID_HOME_BUTTON_TOGGLE_DEVICE2 = get_Ids('home', 't1')
ID_HOME_BUTTON_TOGGLE_DEVICE3 = get_Ids('home', 't2')
ID_HOME_BUTTON_TOGGLE_DEVICE4 = get_Ids('home', 't3')
ID_HOME_BUTTON_TOGGLE_DEVICE5 = get_Ids('home', 't4')
ID_HOME_BUTTON_TOGGLE_DEVICE6 = get_Ids('home', 't5')
ID_HOME_BUTTON_TOGGLE_DEVICE7 = get_Ids('home', 't6')
ID_HOME_BUTTON_TOGGLE_DEVICE8 = get_Ids('home', 't7')

# Device 1 page
ID_BUTTON_TOGGLE_DEVICE1 = get_Ids('Device 1', 'b0')
ID_DEVICE1_REFRESH = get_Ids('Device 1', 'b1')
ID_DEVICE1_VOLTAGE = get_Ids('Device 1', 't13')
ID_DEVICE1_CURRENT = get_Ids('Device 1', 't14')
ID_DEVICE1_PEAK_CURRENT = get_Ids('Device 1', 't15')
ID_DEVICE1_POWER_FACTOR = get_Ids('Device 1', 't16')
ID_DEVICE1_APPARENT_POWER = get_Ids('Device 1', 't17')
ID_DEVICE1_ACTIVE_POWER = get_Ids('Device 1', 't18')
ID_DEVICE1_IMAGINARY_POWER = get_Ids('Device 1', 't19')

# Device 2 page
ID_BUTTON_TOGGLE_DEVICE2 = get_Ids('Device 2', 'b0')
ID_DEVICE2_REFRESH = get_Ids('Device 2', 'b1')
ID_DEVICE2_VOLTAGE = get_Ids('Device 2', 't13')
ID_DEVICE2_CURRENT = get_Ids('Device 2', 't14')
ID_DEVICE2_PEAK_CURRENT = get_Ids('Device 2', 't15')
ID_DEVICE2_POWER_FACTOR = get_Ids('Device 2', 't16')
ID_DEVICE2_APPARENT_POWER = get_Ids('Device 2', 't17')
ID_DEVICE2_ACTIVE_POWER = get_Ids('Device 2', 't18')
ID_DEVICE2_IMAGINARY_POWER = get_Ids('Device 2', 't19')

# Device 3 page
ID_BUTTON_TOGGLE_DEVICE3 = get_Ids('Device 3', 'b0')
ID_DEVICE3_REFRESH = get_Ids('Device 3', 'b1')
ID_DEVICE3_VOLTAGE = get_Ids('Device 3', 't13')
ID_DEVICE3_CURRENT = get_Ids('Device 3', 't14')
ID_DEVICE3_PEAK_CURRENT = get_Ids('Device 3', 't15')
ID_DEVICE3_POWER_FACTOR = get_Ids('Device 3', 't16')
ID_DEVICE3_APPARENT_POWER = get_Ids('Device 3', 't17')
ID_DEVICE3_ACTIVE_POWER = get_Ids('Device 3', 't18')
ID_DEVICE3_IMAGINARY_POWER = get_Ids('Device 3', 't19')

# Device 4 page
ID_BUTTON_TOGGLE_DEVICE4 = get_Ids('Device 4', 'b0')
ID_DEVICE4_REFRESH = get_Ids('Device 4', 'b1')
ID_DEVICE4_VOLTAGE = get_Ids('Device 4', 't13')
ID_DEVICE4_CURRENT = get_Ids('Device 4', 't14')
ID_DEVICE4_PEAK_CURRENT = get_Ids('Device 4', 't15')
ID_DEVICE4_POWER_FACTOR = get_Ids('Device 4', 't16')
ID_DEVICE4_APPARENT_POWER = get_Ids('Device 4', 't17')
ID_DEVICE4_ACTIVE_POWER = get_Ids('Device 4', 't18')
ID_DEVICE4_IMAGINARY_POWER = get_Ids('Device 4', 't19')

# Device 5 page
ID_BUTTON_TOGGLE_DEVICE5 = get_Ids('Device 5', 'b0')
ID_DEVICE5_REFRESH = get_Ids('Device 5', 'b1')
ID_DEVICE5_VOLTAGE = get_Ids('Device 5', 't13')
ID_DEVICE5_CURRENT = get_Ids('Device 5', 't14')
ID_DEVICE5_PEAK_CURRENT = get_Ids('Device 5', 't15')
ID_DEVICE5_POWER_FACTOR = get_Ids('Device 5', 't16')
ID_DEVICE5_APPARENT_POWER = get_Ids('Device 5', 't17')
ID_DEVICE5_ACTIVE_POWER = get_Ids('Device 5', 't18')
ID_DEVICE5_IMAGINARY_POWER = get_Ids('Device 5', 't19')

# Device 6 page
ID_BUTTON_TOGGLE_DEVICE6 = get_Ids('Device 6', 'b0')
ID_DEVICE6_REFRESH = get_Ids('Device 6', 'b1')
ID_DEVICE6_VOLTAGE = get_Ids('Device 6', 't13')
ID_DEVICE6_CURRENT = get_Ids('Device 6', 't14')
ID_DEVICE6_PEAK_CURRENT = get_Ids('Device 6', 't15')
ID_DEVICE6_POWER_FACTOR = get_Ids('Device 6', 't16')
ID_DEVICE6_APPARENT_POWER = get_Ids('Device 6', 't17')
ID_DEVICE6_ACTIVE_POWER = get_Ids('Device 6', 't18')
ID_DEVICE6_IMAGINARY_POWER = get_Ids('Device 6', 't19')

# Device 7 page
ID_BUTTON_TOGGLE_DEVICE7 = get_Ids('Device 7', 'b0')
ID_DEVICE7_REFRESH = get_Ids('Device 7', 'b1')
ID_DEVICE7_VOLTAGE = get_Ids('Device 7', 't13')
ID_DEVICE7_CURRENT = get_Ids('Device 7', 't14')
ID_DEVICE7_PEAK_CURRENT = get_Ids('Device 7', 't15')
ID_DEVICE7_POWER_FACTOR = get_Ids('Device 7', 't16')
ID_DEVICE7_APPARENT_POWER = get_Ids('Device 7', 't17')
ID_DEVICE7_ACTIVE_POWER = get_Ids('Device 7', 't18')
ID_DEVICE7_IMAGINARY_POWER = get_Ids('Device 7', 't19')

# Device 8 page
ID_BUTTON_TOGGLE_DEVICE8 = get_Ids('Device 8', 'b0')
ID_DEVICE8_REFRESH = get_Ids('Device 8', 'b1')
ID_DEVICE8_VOLTAGE = get_Ids('Device 8', 't13')
ID_DEVICE8_CURRENT = get_Ids('Device 8', 't14')
ID_DEVICE8_PEAK_CURRENT = get_Ids('Device 8', 't15')
ID_DEVICE8_POWER_FACTOR = get_Ids('Device 8', 't16')
ID_DEVICE8_APPARENT_POWER = get_Ids('Device 8', 't17')
ID_DEVICE8_ACTIVE_POWER = get_Ids('Device 8', 't18')
ID_DEVICE8_IMAGINARY_POWER = get_Ids('Device 8', 't19')

#lookup tables
ID_HOME_BUTTON_TOGGLE_DEVICES = [ID_HOME_BUTTON_TOGGLE_DEVICE1, ID_HOME_BUTTON_TOGGLE_DEVICE2, ID_HOME_BUTTON_TOGGLE_DEVICE3, ID_HOME_BUTTON_TOGGLE_DEVICE4, ID_HOME_BUTTON_TOGGLE_DEVICE5, ID_HOME_BUTTON_TOGGLE_DEVICE6, ID_HOME_BUTTON_TOGGLE_DEVICE7, ID_HOME_BUTTON_TOGGLE_DEVICE8]
ID_BUTTON_TOGGLE_DEVICES = [ID_BUTTON_TOGGLE_DEVICE1, ID_BUTTON_TOGGLE_DEVICE2, ID_BUTTON_TOGGLE_DEVICE3, ID_BUTTON_TOGGLE_DEVICE4, ID_BUTTON_TOGGLE_DEVICE5, ID_BUTTON_TOGGLE_DEVICE6, ID_BUTTON_TOGGLE_DEVICE7, ID_BUTTON_TOGGLE_DEVICE8]
