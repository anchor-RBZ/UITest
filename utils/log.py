import logging
import os
from logging.handlers import RotatingFileHandler

from config import LOG_DIR


def setup_logger(name, log_file, level=logging.INFO):
    """Function to set up a logger that writes to both console and file."""
    # Create a logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create a console handler and set level to debug
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    # Create a file handler and set level to debug
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    file_handler = RotatingFileHandler(log_file, maxBytes=1024 * 1024 * 5, backupCount=5)
    file_handler.setLevel(level)

    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Add formatter to console_handler and file_handler
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add console_handler and file_handler to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


log_file = os.path.join(LOG_DIR, 'app.log')
logger = setup_logger('my_logger', log_file)

# Example usage
if __name__ == "__main__":
    log_file = os.path.join(LOG_DIR, 'app.log')
    logger = setup_logger('my_logger', log_file)

    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')
