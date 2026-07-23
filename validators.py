from typing import Any, Dict


def is_positive_integer(value: Any) -> bool:
    """
    Checks if the given value is a positive integer.

    Args:
        value (Any): The value to check.

    Returns:
        bool: True if value is a positive integer, False otherwise.
    """
    if isinstance(value, int) and value > 0:
        return True
    return False


def validate_player_data(data: Dict[str, Any]) -> bool:
    """
    Validates player data to ensure it meets criteria.

    Args:
        data (Dict[str, Any]): The player data dictionary to validate.

    Returns:
        bool: True if validation passes, False otherwise.
    """
    required_keys = ['name', 'age', 'score']
    for key in required_keys:
        if key not in data:
            return False
    
    if not isinstance(data['name'], str) or len(data['name']) == 0:
        return False
    if not is_positive_integer(data['age']):
        return False
    if not isinstance(data['score'], (int, float)) or data['score'] < 0:
        return False
    return True
