import json
import os

def load_config(file_path='config.json', defaults=None):
    if defaults is None:
        defaults = {}
    if not os.path.exists(file_path):
        return defaults
    with open(file_path, 'r') as config_file:
        config = json.load(config_file)
    return {**defaults, **config}

if __name__ == '__main__':
    default_settings = {'volume': 50, 'resolution': '1920x1080'}
    settings = load_config('config.json', default_settings)
    print(settings)