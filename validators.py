def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string.')
    if len(user_input) == 0:
        raise ValueError('Input cannot be empty.')
    if len(user_input) > 100:
        raise ValueError('Input must not exceed 100 characters.')
    return True

if __name__ == '__main__':
    while True:
        user_input = input('Enter a command: ')
        try:
            validate_input(user_input)
            print('Valid input:', user_input)
        except ValueError as e:
            print('Invalid input:', e)