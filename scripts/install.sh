#!/bin/bash

# Installation script for Pill Dispenser

echo "Installing Pill Dispenser..."

# Update system
sudo apt-get update
sudo apt-get upgrade -y

# Install Python dependencies
pip3 install -r requirements.txt

# Install system dependencies for touchscreen
sudo apt-get install -y python3-dev python3-pip python3-rpi.gpio
sudo apt-get install -y libsdl2-dev libsdl2-ttf-dev libsdl2-image-dev libsdl2-mixer-dev

# Enable I2C
sudo raspi-config nonint do_i2c 0

# Set up touchscreen
sudo apt-get install -y xinput-calibrator tslib

echo "Installation complete. Please reboot the system."