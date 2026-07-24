import json
from pathlib import Path

def load_config(file_path, defaults):
    config_path = Path(file_path)
    if config_path.is_file():
        with open(config_path) as config_file:
            config = json.load(config_file)
    else:
        config = {}  
    combined_config = {**defaults, **config}
    return combined_config

def save_config(file_path, config):
    with open(file_path, 'w') as config_file:
        json.dump(config, config_file, indent=4)

# Example usage
if __name__ == '__main__':
    defaults = {'setting1': 'value1', 'setting2': 'value2'}
    config = load_config('config.json', defaults)
    print(config)