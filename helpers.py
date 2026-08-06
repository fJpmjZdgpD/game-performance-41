def validate_input(user_input):
    if isinstance(user_input, str) and user_input.strip():
        return True
    return False

def main_loop():
    while True:
        user_input = input('Enter command: ')
        if validate_input(user_input):
            process_input(user_input)
        else:
            print('Invalid input, please try again.')

if __name__ == '__main__':
    main_loop()