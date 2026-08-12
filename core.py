import sys
from validators import validate_input

def main_loop():
    while True:
        user_input = input('Enter a command: ')
        if validate_input(user_input):
            process_command(user_input)
        else:
            print('Invalid input. Please try again.')

def process_command(command):
    if command == 'exit':
        print('Exiting...')
        sys.exit(0)
    print(f'Processing command: {command}')

if __name__ == '__main__':
    main_loop()