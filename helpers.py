import json

def load_game_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def save_game_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def update_game_score(game_data, player_id, score):
    player = game_data.get('players', {}).get(player_id)
    if player:
        player['score'] += score
    else:
        raise ValueError('Player not found')


def get_top_players(game_data, count=5):
    players = game_data.get('players', {}).values()
    sorted_players = sorted(players, key=lambda p: p['score'], reverse=True)
    return sorted_players[:count]