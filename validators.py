def validate_positive_integer(value):
    if not isinstance(value, int):
        raise ValueError('Value must be an integer')
    if value < 0:
        raise ValueError('Value must be positive')
    return True


def validate_non_empty_string(value):
    if not isinstance(value, str):
        raise ValueError('Value must be a string')
    if not value.strip():
        raise ValueError('Value must not be empty')
    return True


def validate_percentage(value):
    if not isinstance(value, (int, float)):
        raise ValueError('Value must be a number')
    if not (0 <= value <= 100):
        raise ValueError('Value must be between 0 and 100')
    return True


def validate_non_negative_float(value):
    if not isinstance(value, (float, int)):
        raise ValueError('Value must be a number')
    if value < 0:
        raise ValueError('Value must be non-negative')
    return True