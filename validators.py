import json

class GameDataValidator:
    @staticmethod
    def validate_score(score):
        if not isinstance(score, (int, float)) or score < 0:
            raise ValueError("Score must be a non-negative number.")

    @staticmethod
    def validate_level(level):
        if not isinstance(level, int) or level < 0:
            raise ValueError("Level must be a non-negative integer.")

    @staticmethod
    def validate_player_name(name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Player name must be a non-empty string.")

    @staticmethod
    def validate_game_data(data):
        GameDataValidator.validate_score(data.get('score', 0))
        GameDataValidator.validate_level(data.get('level', 0))
        GameDataValidator.validate_player_name(data.get('player_name', ''))

    @staticmethod
    def from_json(json_string):
        try:
            data = json.loads(json_string)
            GameDataValidator.validate_game_data(data)
            return data
        except (ValueError, json.JSONDecodeError) as e:
            raise ValueError(f"Invalid game data: {e}")