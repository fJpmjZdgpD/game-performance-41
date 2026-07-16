def validate_player_id(player_id):
    if not isinstance(player_id, int) or player_id < 0:
        raise ValueError("Invalid player ID")
    return True

def validate_score(score):
    if not isinstance(score, (int, float)) or score < 0:
        raise ValueError("Invalid score")
    return True

class GameValidator:
    @staticmethod
    def validate_game_data(game_data):
        if not isinstance(game_data, dict):
            raise ValueError("Game data must be a dictionary")
        required_keys = ['player_id', 'score']
        for key in required_keys:
            if key not in game_data:
                raise ValueError(f"Missing required key: {key}")
        validate_player_id(game_data['player_id'])
        validate_score(game_data['score'])
        return True

    @staticmethod
    def validate_level(level):
        if not isinstance(level, int) or level < 1:
            raise ValueError("Level must be a positive integer")
        return True