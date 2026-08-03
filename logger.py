import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file, max_bytes=10*1024*1024, backup_count=5):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

logger = setup_logger('game.log')
logger.info('Logger setup complete')