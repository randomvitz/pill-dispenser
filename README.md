# Pill Dispenser

A Raspberry Pi-based automatic pill dispenser with touchscreen interface.

## Overview

This project implements an automated pill dispensing system using Raspberry Pi. It features:
- Scheduled dispensing based on user-defined times
- Touchscreen GUI for configuration and monitoring
- Hardware control for servo motors and water pump
- Logging and error handling

## Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the installer: `./scripts/install.sh`
3. Configure hardware pins in `src/config.py`
4. Start the application: `python src/main.py`

## Hardware Requirements

- Raspberry Pi (any model with GPIO)
- 6-module servo controller (PWM)
- Continuous servo for water pump
- Touchscreen display
- Servo motors for pill compartments
- Water pump servo

## Usage

The application runs as a service. Use the touchscreen to set schedules and monitor dispensing.