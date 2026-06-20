def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError("Input must be a string")
    if len(user_input) == 0:
        raise ValueError("Input cannot be empty")
    if not all(c.isalnum() or c.isspace() for c in user_input):
        raise ValueError("Input can only contain alphanumeric characters and spaces")


def validate_game_input(game_input):
    if not isinstance(game_input, dict):
        raise ValueError("Game input must be a dictionary")
    required_keys = ['player_name', 'score']
    for key in required_keys:
        if key not in game_input:
            raise ValueError(f"Missing required key: {key}")
    validate_input(game_input['player_name'])
    if not isinstance(game_input['score'], int) or game_input['score'] < 0:
        raise ValueError("Score must be a non-negative integer")

