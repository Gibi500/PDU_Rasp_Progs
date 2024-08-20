#!/bin/bash

if [ "$(id -u)" != 0 ]; then
  echo 'Sorry, you need to run this script with sudo'
  exit 1
fi

echo '>>> Disable serial console'
sudo raspi-config nonint do_serial 1
sleep 2
echo '>>> Configure UART/Bluetooth'
if grep -q 'enable_uart=1' /boot/config.txt; then
  echo 'Seems Uart already enabled in 14/15 pins, skip this step.'
else
  echo 'enable_uart=1' >> /boot/config.txt
fi
if grep -q 'dtoverlay=pi3-disable-bt' /boot/config.txt; then
  echo 'Seems bluetooth on 14/15 already disabled, skip this step.'
else
  echo 'dtoverlay=pi3-disable-bt' >> /boot/config.txt
fi

echo '>>> Rebooting'

sudo reboot
