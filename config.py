import json
import os

DEFAULTS = {
    'window_size': (800, 600),
    'fullscreen': False,
    'fps': 60,
    'volume': 0.5,
}

class ConfigLoader:
    def __init__(self, filename='config.json'):
        self.filename = filename
        self.config = DEFAULTS.copy()
        self.load_config()

    def load_config(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                user_config = json.load(file)
                self.config.update(user_config)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value
        self.save_config()

    def save_config(self):
        with open(self.filename, 'w') as file:
            json.dump(self.config, file, indent=4)