import json
import os

def load_config(file_path='config.json', defaults=None):
    if defaults is None:
        defaults = {}
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            config = json.load(f)
            return {**defaults, **config}
    return defaults

if __name__ == '__main__':
    defaults = {'setting1': 'default1', 'setting2': 'default2'}
    config = load_config(defaults=defaults)
    print(config)