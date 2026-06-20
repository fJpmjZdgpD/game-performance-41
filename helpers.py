import random

def get_random_item(items):
    return random.choice(items)


def shuffle_list(items):
    random.shuffle(items)
    return items


def calculate_average(scores):
    return sum(scores) / len(scores) if scores else 0


def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)


def load_json(file_path):
    import json
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(file_path, data):
    import json
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
