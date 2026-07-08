import json
from typing import Any, Dict, List

def load_game_data(file_path: str) -> List[Dict[str, Any]]:
    with open(file_path, 'r') as file:
        return json.load(file)


def save_game_data(file_path: str, data: List[Dict[str, Any]]) -> None:
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def filter_game_data(data: List[Dict[str, Any]], key: str, value: Any) -> List[Dict[str, Any]]:
    return [entry for entry in data if entry.get(key) == value]


def aggregate_game_data(data: List[Dict[str, Any]], key: str) -> Dict[Any, int]:
    result = {}
    for entry in data:
        result[entry[key]] = result.get(entry[key], 0) + 1
    return result
