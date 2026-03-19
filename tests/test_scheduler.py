"""
Unit tests for scheduler modules.
"""

import unittest
from unittest.mock import Mock, patch
from src.scheduler.timer import TimerService
from src.scheduler.dispenser import Dispenser
from src.config import Config

class TestTimerService(unittest.TestCase):
    def setUp(self):
        self.config = Mock()
        self.config.get_schedule.return_value = [{'time': '12:00', 'compartments': [1]}]

    @patch('src.scheduler.timer.Dispenser')
    def test_timer_service_init(self, mock_dispenser):
        service = TimerService(self.config)
        self.assertIsNotNone(service.dispenser)

class TestDispenser(unittest.TestCase):
    def setUp(self):
        self.config = Mock()
        self.config.settings = {'water_amount': 50}

    @patch('src.scheduler.dispenser.PWMServoController')
    @patch('src.scheduler.dispenser.WaterPumpController')
    def test_dispenser_init(self, mock_pump, mock_servo):
        dispenser = Dispenser(self.config)
        mock_servo.assert_called_once()
        mock_pump.assert_called_once()

    @patch('src.scheduler.dispenser.PWMServoController')
    @patch('src.scheduler.dispenser.WaterPumpController')
    def test_dispense(self, mock_pump, mock_servo):
        dispenser = Dispenser(self.config)
        dispenser.dispense([1, 2])
        dispenser.servo_controller.dispense_pill.assert_called()

if __name__ == '__main__':
    unittest.main()