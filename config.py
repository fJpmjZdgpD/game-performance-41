import json
import os

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.config = self.load_config()

    def load_config(self):
        config_path = 'config.json'
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                user_config = json.load(f)
            return {**self.default_config, **user_config}
        return self.default_config

    def get(self, key, default=None):
        return self.config.get(key, default)

# Example usage
if __name__ == '__main__':
    defaults = {'setting1': True, 'setting2': 'default_value'}
    config_loader = ConfigLoader(defaults)
    print(config_loader.get('setting1'))
    print(config_loader.get('setting2'))
    print(config_loader.get('non_existent', 'fallback'))