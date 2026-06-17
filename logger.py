import logging


def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Sets up a logger with the specified name and logging level.

    Args:
        name (str): The name for the logger.
        level (int): The logging level (default: logging.INFO).

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    handler = logging.StreamHandler()
    handler.setLevel(level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


def log_exception(logger: logging.Logger, exception: Exception) -> None:
    """Logs an exception message using the provided logger.

    Args:
        logger (logging.Logger): The logger instance to use.
        exception (Exception): The exception to log.
    """
    logger.error('An exception occurred', exc_info=exception)