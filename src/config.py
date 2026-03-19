"""
Configuration management for the Pill Dispenser.
Loads and saves user settings and dispensing schedules.
"""

import json
import os
from datetime import time

class Config:
    def __init__(self, config_file='config.json'):
        self.config_file = os.path.join(os.path.dirname(__file__), config_file)
        self.settings = self.load_config()

    def load_config(self):
        """Load configuration from file, or create default if not exists."""
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                return json.load(f)
        else:
            # Default configuration
            default_config = {
                'hardware': {
                    'servo_pins': [18, 19, 20, 21, 22, 23],  # PWM pins
                    'screen_i2c': {'sda': 20, 'scl': 21}
                },
                'schedules': [
                    {'time': '08:00', 'compartments': [1, 2]},
                    {'time': '12:00', 'compartments': [3, 4]},
                    {'time': '18:00', 'compartments': [5, 6]}
                ],
                'water_amount': 50  # ml per dispensing
            }
            self.save_config(default_config)
            return default_config

    def save_config(self, config=None):
        """Save configuration to file."""
        if config:
            self.settings = config
        with open(self.config_file, 'w') as f:
            json.dump(self.settings, f, indent=2)

    def get_schedule(self):
        """Get dispensing schedule."""
        return self.settings.get('schedules', [])

    def set_schedule(self, schedule):
        """Set dispensing schedule."""
        self.settings['schedules'] = schedule
        self.save_config()

    def get_hardware_config(self):
        """Get hardware configuration."""
        return self.settings.get('hardware', {})