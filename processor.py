import sys

def process_input(user_input):
    valid_inputs = {'start', 'stop', 'pause', 'resume'}
    if user_input not in valid_inputs:
        raise ValueError('Invalid input provided.')
    return user_input

def main_loop():
    while True:
        try:
            user_input = input('Enter command: ').strip().lower()
            command = process_input(user_input)
            if command == 'start':
                print('Game started.')
            elif command == 'stop':
                print('Game stopped.')
                break
            elif command == 'pause':
                print('Game paused.')
            elif command == 'resume':
                print('Game resumed.')
        except ValueError as e:
            print(e)
            print('Please try again.')

if __name__ == '__main__':
    main_loop()