import logging


def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Set up a logger with the specified name and log level."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


def log_info(logger: logging.Logger, message: str) -> None:
    """Log an informational message using the specified logger."""
    logger.info(message)


def log_error(logger: logging.Logger, message: str) -> None:
    """Log an error message using the specified logger."""
    logger.error(message)


if __name__ == '__main__':
    my_logger = setup_logger('game_logger')
    log_info(my_logger, 'Game started')
    log_error(my_logger, 'An error occurred')