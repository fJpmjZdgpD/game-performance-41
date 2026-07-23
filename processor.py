import sys
import random

class GameProcessor:
    def __init__(self):
        self.score = 0

    def process_input(self, user_input):
        if not self.validate_input(user_input):
            print('Invalid input. Please enter a number between 1 and 10.')
            return
        self.score += user_input
        print(f'Score updated: {self.score}')

    def validate_input(self, user_input):
        try:
            value = int(user_input)
            return 1 <= value <= 10
        except ValueError:
            return False

    def main_loop(self):
        print('Enter a number between 1 and 10:')
        while True:
            user_input = input('> ')
            if user_input.lower() == 'exit':
                print('Exiting game. Final score:', self.score)
                sys.exit(0)
            self.process_input(user_input)

if __name__ == '__main__':
    game = GameProcessor()
    game.main_loop()