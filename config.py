import json

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.config = default_config.copy()

    def load(self, filepath):
        try:
            with open(filepath, 'r') as file:
                user_config = json.load(file)
            self.config.update(user_config)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def get(self, key, default=None):
        return self.config.get(key, default)