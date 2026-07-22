import logging
from logging.handlers import RotatingFileHandler

class Logger:
    def __init__(self, filename='app.log', max_bytes=10485760, backup_count=5):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        handler = RotatingFileHandler(filename, maxBytes=max_bytes, backupCount=backup_count)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def get_logger(self):
        return self.logger

logger = Logger().get_logger()