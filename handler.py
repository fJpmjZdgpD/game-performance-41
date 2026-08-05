import json
from constants import MAX_LEVEL, INITIAL_SCORE

class GameHandler:
    def __init__(self):
        self.score = INITIAL_SCORE
        self.level = 1

    def level_up(self):
        if self.level < MAX_LEVEL:
            self.level += 1
            self.score += 100

    def reset_game(self):
        self.score = INITIAL_SCORE
        self.level = 1

    def get_game_state(self):
        return json.dumps({'score': self.score, 'level': self.level})

if __name__ == '__main__':
    game_handler = GameHandler()  
    game_handler.level_up()  
    print(game_handler.get_game_state())