# Wiring Diagram

## Raspberry Pi GPIO Pinout

- GPIO 18: PWM for servo controller (6-module)
- GPIO 19: PWM for water pump servo
- GPIO 20: I2C SDA for touchscreen
- GPIO 21: I2C SCL for touchscreen
- GPIO 22: Reset pin for servo controller
- GPIO 23: Enable pin for servo controller

## Servo Connections

### Pill Compartments (6 servos)
- Servo 1: Compartment 1 - GPIO 18 (PWM channel 0)
- Servo 2: Compartment 2 - GPIO 18 (PWM channel 1)
- Servo 3: Compartment 3 - GPIO 18 (PWM channel 2)
- Servo 4: Compartment 4 - GPIO 18 (PWM channel 3)
- Servo 5: Compartment 5 - GPIO 18 (PWM channel 4)
- Servo 6: Compartment 6 - GPIO 18 (PWM channel 5)

### Water Pump Servo
- Water Pump: GPIO 19 (PWM)

## Touchscreen
- Connected via I2C (GPIO 20 SDA, GPIO 21 SCL)
- Power: 5V and GND from Pi

## Power Supply
- Servos: 5V from Pi or external supply
- Ensure common ground between Pi and servos