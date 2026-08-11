import json
import os

class ConfigLoader:
    def __init__(self, default_config_path, user_config_path):
        self.default_config = self.load_config(default_config_path)
        self.user_config = self.load_config(user_config_path) or {}
        self.config = self.merge_configs(self.default_config, self.user_config)

    def load_config(self, path):
        if not os.path.exists(path):
            return None
        with open(path) as config_file:
            return json.load(config_file)

    def merge_configs(self, default, user):
        merged = default.copy()
        merged.update(user)
        return merged

    def get(self, key, default=None):
        return self.config.get(key, default)

if __name__ == '__main__':
    loader = ConfigLoader('default_config.json', 'user_config.json')
    print(loader.get('setting1', 'default_value'))