"""
PWM Servo Controller for 6-module pill dispenser.
Provides abstraction for controlling multiple servo motors.
"""

import RPi.GPIO as GPIO
import time

class PWMServoController:
    def __init__(self, pwm_pin=18, frequency=50):
        self.pwm_pin = pwm_pin
        self.frequency = frequency
        self.pwm = None
        self.channels = {}  # channel: duty_cycle

    def setup(self):
        """Initialize PWM and GPIO."""
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pwm_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pwm_pin, self.frequency)
        self.pwm.start(0)

    def set_servo_angle(self, channel, angle):
        """Set servo angle for a specific channel (0-5)."""
        if not 0 <= channel <= 5:
            raise ValueError("Channel must be between 0 and 5")

        # Convert angle to duty cycle (2.5% to 12.5% for 0-180 degrees)
        duty_cycle = 2.5 + (angle / 180.0) * 10.0
        self.channels[channel] = duty_cycle

        # For simplicity, assume single PWM pin controls all via multiplexing
        # In reality, might need PCA9685 or similar for multiple channels
        self.pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(0.5)  # Allow servo to move
        self.pwm.ChangeDutyCycle(0)  # Stop PWM to prevent jitter

    def dispense_pill(self, compartment):
        """Dispense pill from specific compartment."""
        # Rotate servo to open compartment
        self.set_servo_angle(compartment, 90)  # Open position
        time.sleep(1)
        self.set_servo_angle(compartment, 0)   # Close position

    def cleanup(self):
        """Clean up GPIO."""
        if self.pwm:
            self.pwm.stop()
        GPIO.cleanup()