import random
import logging

class GameError(Exception):
    pass

class Game:
    def __init__(self, max_players):
        if not isinstance(max_players, int) or max_players < 1:
            raise GameError('max_players must be a positive integer')
        self.max_players = max_players
        self.players = []

    def add_player(self, player_name):
        if len(self.players) >= self.max_players:
            raise GameError('Cannot add more players than max_players')
        if player_name in self.players:
            raise GameError('Player already exists')
        self.players.append(player_name)

    def start_game(self):
        if len(self.players) < 2:
            raise GameError('At least 2 players are required to start the game')
        logging.info('Game is starting with players: %s', self.players)

    def get_random_player(self):
        if not self.players:
            raise GameError('No players available')
        return random.choice(self.players)

