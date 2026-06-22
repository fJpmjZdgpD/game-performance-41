import json
import os

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.config = self.load_config()

    def load_config(self):
        config_file = 'config.json'
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                return {**self.default_config, **json.load(f)}
        return self.default_config

    def get(self, key):
        return self.config.get(key, None)

    def set(self, key, value):
        self.config[key] = value
        with open('config.json', 'w') as f:
            json.dump(self.config, f, indent=4)

# Example defaults
default_config = {
    'resolution': '1920x1080',
    'volume': 75,
    'difficulty': 'normal'
}

config_loader = ConfigLoader(default_config)