"""
Logging setup and utilities.
"""

import logging
import logging.handlers
import os

def setup_logging(log_file='pill_dispenser.log', level=logging.INFO):
    """Setup logging configuration."""
    # Create logs directory if it doesn't exist
    log_dir = os.path.join(os.path.dirname(__file__), '..', 'logs')
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, log_file)

    # Create logger
    logger = logging.getLogger()
    logger.setLevel(level)

    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler with rotation
    file_handler = logging.handlers.RotatingFileHandler(
        log_path, maxBytes=1024*1024, backupCount=5
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

def log_error(error, context=None):
    """Log an error with optional context."""
    logger = logging.getLogger(__name__)
    message = f"Error: {error}"
    if context:
        message += f" Context: {context}"
    logger.error(message)

def log_info(message):
    """Log an info message."""
    logger = logging.getLogger(__name__)
    logger.info(message)