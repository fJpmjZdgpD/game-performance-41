def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string')
    if len(user_input) == 0:
        raise ValueError('Input cannot be empty')
    if any(char not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ' for char in user_input):
        raise ValueError('Input contains invalid characters')
    return True

def main_loop():
    while True:
        user_input = input('Enter your command: ')
        try:
            validate_input(user_input)
            process_input(user_input)
        except ValueError as e:
            print(e)

if __name__ == '__main__':
    main_loop()