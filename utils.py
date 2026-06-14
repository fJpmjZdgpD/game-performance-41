import random
import logging

logger = logging.getLogger(__name__)

class InvalidInputError(Exception):
    pass

class InvalidRangeError(Exception):
    pass

def get_random_number(min_value, max_value):
    if not (isinstance(min_value, int) and isinstance(max_value, int)):
        logger.error("Both min_value and max_value must be integers.")
        raise InvalidInputError("Input values must be integers.")
    if min_value >= max_value:
        logger.error("min_value must be less than max_value.")
        raise InvalidRangeError("min_value must be less than max_value.")
    return random.randint(min_value, max_value)

def safe_divide(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        logger.error("Attempted division by zero.")
        return float('inf')
    except TypeError:
        logger.error("Both numerator and denominator must be numbers.")
        raise InvalidInputError("Inputs must be numeric.")

