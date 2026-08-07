def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string')
    if len(user_input) == 0:
        raise ValueError('Input cannot be empty')
    if any(char.isdigit() for char in user_input):
        raise ValueError('Input cannot contain numbers')
    return True

# Usage in main processing loop
try:
    user_input = input('Enter command: ')
    validate_input(user_input)
    # Process valid input here
except ValueError as e:
    print(f'Invalid input: {e}')