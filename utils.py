import json

def load_game_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def save_game_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def update_player_score(data, player_id, score):
    if player_id in data:
        data[player_id]['score'] += score
    else:
        data[player_id] = {'score': score}


def get_top_players(data, top_n=5):
    return sorted(data.items(), key=lambda x: x[1]['score'], reverse=True)[:top_n]
