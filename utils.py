import json

def load_game_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def save_game_data(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)


def update_game_data(filepath, new_data):
    data = load_game_data(filepath)
    data.update(new_data)
    save_game_data(filepath, data)


def delete_game_data(filepath, keys):
    data = load_game_data(filepath)
    for key in keys:
        data.pop(key, None)
    save_game_data(filepath, data)


def validate_game_data(data):
    required_keys = ['title', 'genre', 'release_date']
    return all(key in data for key in required_keys)
