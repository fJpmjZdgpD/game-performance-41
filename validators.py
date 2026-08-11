def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string')
    if len(user_input) == 0:
        raise ValueError('Input cannot be empty')
    return True

def validate_integer(value):
    if not isinstance(value, int):
        raise ValueError('Value must be an integer')
    if value < 0:
        raise ValueError('Value cannot be negative')
    return True

