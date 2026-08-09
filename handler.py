import json

class GameError(Exception):
    pass

class GameHandler:
    def __init__(self):
        self.players = {}

    def add_player(self, player_id, player_data):
        if player_id in self.players:
            raise GameError('Player already exists')
        self.players[player_id] = player_data

    def get_player(self, player_id):
        try:
            return self.players[player_id]
        except KeyError:
            raise GameError('Player not found')

    def update_player(self, player_id, player_data):
        if player_id not in self.players:
            raise GameError('Player not found')
        self.players[player_id] = player_data

    def remove_player(self, player_id):
        try:
            del self.players[player_id]
        except KeyError:
            raise GameError('Player not found')

    def to_json(self):
        return json.dumps(self.players)

    @classmethod
    def from_json(cls, data):
        try:
            players = json.loads(data)
            instance = cls()
            for player_id, player_data in players.items():
                instance.add_player(player_id, player_data)
            return instance
        except (json.JSONDecodeError, TypeError):
            raise GameError('Invalid JSON data')
