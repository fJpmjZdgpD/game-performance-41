import json
import os

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.config = default_config.copy()

    def load_from_file(self, file_path):
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                file_config = json.load(file)
                self.config.update(file_config)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value

# Example usage
if __name__ == '__main__':
    default_config = {
        'volume': 50,
        'resolution': '1920x1080',
        'fullscreen': True
    }
    loader = ConfigLoader(default_config)
    loader.load_from_file('config.json')
    print(loader.get('volume'))
    print(loader.get('fullscreen'))
    loader.set('volume', 75)
    print(loader.get('volume'))