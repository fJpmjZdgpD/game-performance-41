import sys

class GameHandler:
    def __init__(self):
        self.valid_inputs = {'move', 'attack', 'defend', 'run'}

    def validate_input(self, user_input):
        return user_input in self.valid_inputs

    def main_loop(self):
        while True:
            user_input = input('Enter your action: ').strip().lower()
            if not self.validate_input(user_input):
                print('Invalid input, please try again.')
                continue
            self.process_action(user_input)

    def process_action(self, action):
        print(f'Processing action: {action}')  

if __name__ == '__main__':
    handler = GameHandler()
    try:
        handler.main_loop()
    except KeyboardInterrupt:
        sys.exit('Game terminated by user.')