from typing import Any, Dict


def is_positive_integer(value: Any) -> bool:
    """
    Checks if the given value is a positive integer.

    Args:
        value (Any): The value to check.

    Returns:
        bool: True if value is a positive integer, otherwise False.
    """
    return isinstance(value, int) and value > 0


def validate_player_data(data: Dict[str, Any]) -> bool:
    """
    Validates player data to ensure it meets game requirements.

    Args:
        data (Dict[str, Any]): The player data to validate.

    Returns:
        bool: True if data is valid, otherwise False.
    """
    if not isinstance(data, dict):
        return False
    return all([
        'name' in data and isinstance(data['name'], str),
        'age' in data and is_positive_integer(data['age']),
        'score' in data and isinstance(data['score'], (int, float))
    ])


def validate_game_settings(settings: Dict[str, Any]) -> bool:
    """
    Validates the game settings configuration.

    Args:
        settings (Dict[str, Any]): The settings to validate.

    Returns:
        bool: True if settings are valid, otherwise False.
    """
    if not isinstance(settings, dict):
        return False
    return all([
        'difficulty' in settings and settings['difficulty'] in ['easy', 'medium', 'hard'],
        'max_players' in settings and is_positive_integer(settings['max_players'])
    ])