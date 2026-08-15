import logging


def setup_logger(name: str) -> logging.Logger:
    """Create and configure a logger."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def log_info(logger: logging.Logger, message: str) -> None:
    """Log an info message."""
    logger.info(message)


def log_warning(logger: logging.Logger, message: str) -> None:
    """Log a warning message."""
    logger.warning(message)


def log_error(logger: logging.Logger, message: str) -> None:
    """Log an error message."""
    logger.error(message)


def log_debug(logger: logging.Logger, message: str) -> None:
    """Log a debug message."""
    logger.debug(message)
