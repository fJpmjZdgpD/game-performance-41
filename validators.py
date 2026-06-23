import re

def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string.')  
    if len(user_input) == 0:
        raise ValueError('Input cannot be empty.')  
    if not re.match('^[a-zA-Z0-9 ]*$', user_input):
        raise ValueError('Input contains invalid characters.')  
    return True

