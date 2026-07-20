import json

def load_game_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_game_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

class GameDataHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self):
        return load_game_data(self.file_path)

    def save_data(self):
        save_game_data(self.file_path, self.data)

    def update_score(self, player_id, score):
        if player_id in self.data:
            self.data[player_id]['score'] = score
            self.save_data()

    def get_player_data(self, player_id):
        return self.data.get(player_id, None)