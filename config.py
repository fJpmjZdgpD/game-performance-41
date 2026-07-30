import json
import os

DEFAULTS = {
    'resolution': '1920x1080',
    'fullscreen': True,
    'volume': 75,
    'controls': {
        'up': 'W',
        'down': 'S',
        'left': 'A',
        'right': 'D'
    }
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if os.path.isfile(self.config_file):
            with open(self.config_file) as f:
                user_config = json.load(f)
            return self._merge_configs(DEFAULTS, user_config)
        return DEFAULTS

    def _merge_configs(self, defaults, user_config):
        config = defaults.copy()
        config.update(user_config)
        return config

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)