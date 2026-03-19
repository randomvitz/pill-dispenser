"""
Dispenser Coordinator.
Coordinates servo motors and water pump for pill dispensing.
"""

import logging
from hardware.pwm_servo import PWMServoController
from hardware.water_pump import WaterPumpController

logger = logging.getLogger(__name__)

class Dispenser:
    def __init__(self, config):
        self.config = config
        self.servo_controller = PWMServoController()
        self.water_pump = WaterPumpController()
        self.servo_controller.setup()
        self.water_pump.setup()

    def dispense(self, compartments):
        """Dispense pills from specified compartments."""
        logger.info(f"Dispensing from compartments: {compartments}")

        for compartment in compartments:
            try:
                self.servo_controller.dispense_pill(compartment)
                logger.info(f"Dispensed from compartment {compartment}")
            except Exception as e:
                logger.error(f"Error dispensing from compartment {compartment}: {e}")

        # Dispense water after pills
        try:
            water_amount = self.config.settings.get('water_amount', 50)
            duration = water_amount / 10  # Assume 10ml per second
            self.water_pump.dispense_water(duration)
            logger.info("Water dispensed")
        except Exception as e:
            logger.error(f"Error dispensing water: {e}")

    def manual_dispense(self, compartment):
        """Manual dispense from single compartment."""
        self.dispense([compartment])

    def cleanup(self):
        """Clean up hardware."""
        self.servo_controller.cleanup()
        self.water_pump.cleanup()