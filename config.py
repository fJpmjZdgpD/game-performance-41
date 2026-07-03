import os

class ConfigError(Exception):
    pass

def load_config(file_path):
    if not os.path.isfile(file_path):
        raise ConfigError(f'Config file not found: {file_path}')
    try:
        with open(file_path, 'r') as config_file:
            config_data = config_file.read()
            return parse_config(config_data)
    except IOError as e:
        raise ConfigError(f'Error reading config file: {e}')

def parse_config(data):
    config = {}
    for line in data.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        key, value = line.split('=', 1)
        config[key.strip()] = value.strip()
    return config
