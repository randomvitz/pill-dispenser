"""
Mock hardware tests for development without physical hardware.
"""

import unittest
from unittest.mock import Mock, patch
from src.hardware.pwm_servo import PWMServoController
from src.hardware.water_pump import WaterPumpController

class TestPWMServoController(unittest.TestCase):
    @patch('src.hardware.pwm_servo.GPIO')
    def test_setup(self, mock_gpio):
        controller = PWMServoController()
        controller.setup()
        mock_gpio.setmode.assert_called_with(mock_gpio.BCM)
        mock_gpio.setup.assert_called()

    @patch('src.hardware.pwm_servo.GPIO')
    def test_set_servo_angle(self, mock_gpio):
        controller = PWMServoController()
        controller.setup()
        controller.set_servo_angle(0, 90)
        # Verify PWM duty cycle changes
        self.assertIn(0, controller.channels)

class TestWaterPumpController(unittest.TestCase):
    @patch('src.hardware.water_pump.GPIO')
    def test_setup(self, mock_gpio):
        pump = WaterPumpController()
        pump.setup()
        mock_gpio.setmode.assert_called_with(mock_gpio.BCM)

    @patch('src.hardware.water_pump.GPIO')
    @patch('src.hardware.water_pump.time')
    def test_dispense_water(self, mock_time, mock_gpio):
        pump = WaterPumpController()
        pump.setup()
        pump.dispense_water(2)
        mock_time.sleep.assert_called_with(2)

if __name__ == '__main__':
    unittest.main()