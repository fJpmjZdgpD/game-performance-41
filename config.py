import json
import os

DEFAULT_CONFIG = {
    'resolution': '1920x1080',
    'fullscreen': True,
    'volume': 75,
    'controls': {
        'move_forward': 'W',
        'move_back': 'S',
        'move_left': 'A',
        'move_right': 'D',
        'jump': 'SPACE'
    }
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                user_config = json.load(file)
                return {**DEFAULT_CONFIG, **user_config}
        return DEFAULT_CONFIG

    def get(self, key, default=None):
        return self.config.get(key, default)

if __name__ == '__main__':
    loader = ConfigLoader()
    print(loader.config)