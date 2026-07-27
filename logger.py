import logging
import os
from logging.handlers import RotatingFileHandler

LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_LEVEL = logging.INFO
LOG_FILE = 'game_performance.log'
MAX_BYTES = 5 * 1024 * 1024
BACKUP_COUNT = 3


def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)

    if not logger.hasHandlers():
        handler = RotatingFileHandler(LOG_FILE, maxBytes=MAX_BYTES, backupCount=BACKUP_COUNT)
        formatter = logging.Formatter(LOG_FORMAT)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

if __name__ == '__main__':
    log = setup_logger(__name__)
    log.info('Logger is set up and ready.')