def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string')
    if len(user_input) == 0:
        raise ValueError('Input cannot be empty')
    if user_input not in ['start', 'stop', 'pause', 'resume']:
        raise ValueError('Invalid command')

if __name__ == '__main__':
    while True:
        user_input = input('Enter a command: ')
        try:
            validate_input(user_input)
            print(f'Valid input received: {user_input}')
        except ValueError as e:
            print(f'Error: {e}')