"""
Unit tests for config module.
"""

import unittest
import os
import json
from src.config import Config

class TestConfig(unittest.TestCase):
    def setUp(self):
        self.test_config_file = 'test_config.json'
        # Remove test file if exists
        if os.path.exists(self.test_config_file):
            os.remove(self.test_config_file)

    def tearDown(self):
        # Clean up test file
        if os.path.exists(self.test_config_file):
            os.remove(self.test_config_file)

    def test_load_default_config(self):
        config = Config(self.test_config_file)
        self.assertIsNotNone(config.settings)
        self.assertIn('hardware', config.settings)
        self.assertIn('schedules', config.settings)

    def test_save_and_load_config(self):
        config = Config(self.test_config_file)
        test_settings = {'test': 'value'}
        config.save_config(test_settings)

        # Load new instance
        config2 = Config(self.test_config_file)
        self.assertEqual(config2.settings, test_settings)

    def test_get_schedule(self):
        config = Config(self.test_config_file)
        schedule = config.get_schedule()
        self.assertIsInstance(schedule, list)

    def test_set_schedule(self):
        config = Config(self.test_config_file)
        new_schedule = [{'time': '10:00', 'compartments': [1, 2]}]
        config.set_schedule(new_schedule)
        self.assertEqual(config.get_schedule(), new_schedule)

if __name__ == '__main__':
    unittest.main()