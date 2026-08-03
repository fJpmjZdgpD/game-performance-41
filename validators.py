def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string')
    if not user_input:
        raise ValueError('Input cannot be empty')
    return True

def validate_game_action(action):
    valid_actions = ['move', 'attack', 'defend']
    if action not in valid_actions:
        raise ValueError(f'Invalid action. Choose from: {valid_actions}')
    return True

