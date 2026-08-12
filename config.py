import json
import os

class ConfigLoader:
    def __init__(self, default_config_path, user_config_path):
        self.default_config = self.load_config(default_config_path)
        self.user_config = self.load_config(user_config_path)

    def load_config(self, path):
        if not os.path.exists(path):
            return {}
        with open(path, 'r') as file:
            return json.load(file)

    def get_config(self):
        config = self.default_config.copy()
        config.update(self.user_config)
        return config

if __name__ == '__main__':
    config_loader = ConfigLoader('default_config.json', 'user_config.json')
    config = config_loader.get_config()
    print(config)