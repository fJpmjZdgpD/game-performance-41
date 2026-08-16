import json
from typing import Any, Dict, List

class GameDataHandler:
    def __init__(self, data: Dict[str, Any]) -> None:
        self.data = data

    def to_json(self) -> str:
        return json.dumps(self.data)

    def from_json(self, json_str: str) -> None:
        self.data = json.loads(json_str)

    def get_game_stats(self, game_id: str) -> Dict[str, Any]:
        return self.data.get(game_id, {})

    def update_game_stats(self, game_id: str, stats: Dict[str, Any]) -> None:
        self.data[game_id] = stats

    def list_games(self) -> List[str]:
        return list(self.data.keys())

# Sample usage:
# handler = GameDataHandler({'game1': {'score': 100}})
# handler.update_game_stats('game2', {'score': 150})
# print(handler.to_json())