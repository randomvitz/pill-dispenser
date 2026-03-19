#!/usr/bin/env python3
"""
Main entry point for the Pill Dispenser application.
Bootstraps the service and starts the GUI and scheduler.
"""

import sys
import os
import logging
from config import Config
from gui.screens import MainScreen
from scheduler.timer import TimerService
from utils.logger import setup_logging

def main():
    # Setup logging
    setup_logging()
    logger = logging.getLogger(__name__)

    try:
        # Load configuration
        config = Config()
        logger.info("Configuration loaded")

        # Start timer service
        timer_service = TimerService(config)
        timer_service.start()

        # Start GUI
        main_screen = MainScreen(config, timer_service)
        main_screen.run()

    except KeyboardInterrupt:
        logger.info("Application interrupted by user")
    except Exception as e:
        logger.error(f"Application error: {e}")
        sys.exit(1)
    finally:
        logger.info("Application shutting down")

if __name__ == "__main__":
    main()