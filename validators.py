import re

def is_valid_username(username: str) -> bool:
    return bool(re.match(r'^[A-Za-z0-9_]{3,20}$', username))


def is_valid_email(email: str) -> bool:
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email))


def is_valid_score(score: int) -> bool:
    return isinstance(score, int) and 0 <= score <= 100


def validate_game_data(data: dict) -> bool:
    if not ('username' in data and 'email' in data and 'score' in data):
        return False
    return (is_valid_username(data['username']) and
            is_valid_email(data['email']) and
            is_valid_score(data['score']))