from typing import Any, Dict


def is_positive_integer(value: Any) -> bool:
    """
    Validate if the provided value is a positive integer.
    
    Args:
        value (Any): The value to validate.
    
    Returns:
        bool: True if value is a positive integer, otherwise False.
    """
    if isinstance(value, int) and value > 0:
        return True
    return False


def validate_player_data(player_data: Dict[str, Any]) -> bool:
    """
    Validate the structure and content of player data.
    
    Args:
        player_data (Dict[str, Any]): A dictionary containing player data.
    
    Returns:
        bool: True if player data is valid, otherwise False.
    """
    required_keys = ['name', 'score']
    if not all(key in player_data for key in required_keys):
        return False
    if not isinstance(player_data['name'], str) or not is_positive_integer(player_data['score']):
        return False
    return True


def validate_game_settings(settings: Dict[str, Any]) -> bool:
    """
    Validate game settings configuration.
    
    Args:
        settings (Dict[str, Any]): A dictionary containing game settings.
    
    Returns:
        bool: True if settings are valid, otherwise False.
    """
    required_keys = ['difficulty', 'max_players']
    if not all(key in settings for key in required_keys):
        return False
    if settings['difficulty'] not in ['easy', 'medium', 'hard']:
        return False
    if not is_positive_integer(settings['max_players']):
        return False
    return True
