import sys

class InputError(Exception):
    pass

def validate_input(user_input):
    if not isinstance(user_input, str) or not user_input:
        raise InputError('Invalid input: Must be a non-empty string.')
    return user_input

def process_user_input(user_input):
    validate_input(user_input)
    return f'Processed input: {user_input}'

def main_loop():
    while True:
        user_input = input('Enter something (or type quit to exit): ')
        if user_input.lower() == 'quit':
            print('Exiting...')
            break
        try:
            result = process_user_input(user_input)
            print(result)
        except InputError as e:
            print(e)

if __name__ == '__main__':
    main_loop()