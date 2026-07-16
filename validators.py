def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string.')
    if len(user_input) == 0:
        raise ValueError('Input cannot be empty.')
    if len(user_input) > 100:
        raise ValueError('Input must not exceed 100 characters.')
    return user_input

def validate_choice(choice, valid_choices):
    if choice not in valid_choices:
        raise ValueError(f'Choice must be one of: {valid_choices}')
    return choice

