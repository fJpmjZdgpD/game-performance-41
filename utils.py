import json
from typing import Any, Dict, List

def load_game_data(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r') as file:
        return json.load(file)


def save_game_data(file_path: str, data: Dict[str, Any]) -> None:
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def filter_high_scores(scores: List[Dict[str, Any]], threshold: int) -> List[Dict[str, Any]]:
    return [score for score in scores if score['score'] >= threshold]


def calculate_average_score(scores: List[Dict[str, Any]]) -> float:
    if not scores:
        return 0.0
    total_score = sum(score['score'] for score in scores)
    return total_score / len(scores)


def format_player_stats(player: Dict[str, Any]) -> str:
    return f"{player['name']} - Score: {player['score']}, Level: {player['level']}"