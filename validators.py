def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string.')
    if user_input.strip() == '':
        raise ValueError('Input cannot be empty.')
    if len(user_input) > 100:
        raise ValueError('Input exceeds maximum length of 100 characters.')
    return True

def main_loop():
    while True:
        user_input = input('Enter command: ')
        try:
            validate_input(user_input)
            # Process valid input here
        except ValueError as e:
            print(f'Invalid input: {e}')

if __name__ == '__main__':
    main_loop()