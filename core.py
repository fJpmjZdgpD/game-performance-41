import random

class GameError(Exception):
    pass

class Game:
    def __init__(self, max_score):
        if max_score <= 0:
            raise GameError('Max score must be greater than zero.')
        self.max_score = max_score
        self.current_score = 0

    def add_score(self, points):
        if points < 0:
            raise GameError('Score points cannot be negative.')
        self.current_score += points
        self.check_score()

    def check_score(self):
        if self.current_score > self.max_score:
            raise GameError('Current score exceeds max score.')

    def random_event(self):
        event = random.choice(['win', 'lose'])
        if event == 'win':
            self.add_score(random.randint(1, 10))
        else:
            raise GameError('Game lost.')

    def reset(self):
        self.current_score = 0

# Example usage:
if __name__ == '__main__':
    game = Game(50)
    game.random_event()