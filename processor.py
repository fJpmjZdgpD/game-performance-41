import logging
from validators import validate_input

logger = logging.getLogger(__name__)

class GameProcessor:
    def __init__(self):
        self.running = True

    def process_input(self, user_input):
        if validate_input(user_input):
            self.handle_input(user_input)
        else:
            logger.warning(f'Invalid input: {user_input}')

    def handle_input(self, user_input):
        # Handle the valid input accordingly
        logger.info(f'Processing input: {user_input}')

    def main_loop(self):
        while self.running:
            user_input = input('Enter command: ')
            self.process_input(user_input)
            if user_input.lower() == 'exit':
                self.running = False

if __name__ == '__main__':
    processor = GameProcessor()
    processor.main_loop()