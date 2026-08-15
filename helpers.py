import json
import os

def load_game_data(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f'File not found: {file_path}')
    with open(file_path, 'r') as file:
        return json.load(file)


def save_game_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def get_player_score(player_data):
    return player_data.get('score', 0)


def update_player_score(player_data, score):
    player_data['score'] = score
    return player_data


def filter_high_scores(players_data, threshold):
    return [player for player in players_data if player.get('score', 0) > threshold]