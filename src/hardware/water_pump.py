"""
Water Pump Controller using continuous servo.
Controls water dispensing for pill washing.
"""

import RPi.GPIO as GPIO
import time

class WaterPumpController:
    def __init__(self, pwm_pin=19, frequency=50):
        self.pwm_pin = pwm_pin
        self.frequency = frequency
        self.pwm = None

    def setup(self):
        """Initialize PWM and GPIO."""
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pwm_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pwm_pin, self.frequency)
        self.pwm.start(0)

    def dispense_water(self, duration_seconds=5):
        """Dispense water for specified duration."""
        # For continuous servo, 7.5% duty cycle is stop
        # 5% is full speed one direction, 10% the other
        self.pwm.ChangeDutyCycle(5.0)  # Forward direction
        time.sleep(duration_seconds)
        self.pwm.ChangeDutyCycle(7.5)  # Stop

    def set_speed(self, speed_percent):
        """Set pump speed (0-100%)."""
        if not 0 <= speed_percent <= 100:
            raise ValueError("Speed must be between 0 and 100")

        # Map to duty cycle range (5% to 10% for direction)
        duty_cycle = 5.0 + (speed_percent / 100.0) * 5.0
        self.pwm.ChangeDutyCycle(duty_cycle)

    def stop(self):
        """Stop the pump."""
        self.pwm.ChangeDutyCycle(7.5)

    def cleanup(self):
        """Clean up GPIO."""
        if self.pwm:
            self.pwm.stop()
        GPIO.cleanup()