import re

def is_valid_username(username):
    return bool(re.match(r'^[a-zA-Z0-9]{3,20}$', username))


def is_valid_email(email):
    return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))


def is_valid_positive_integer(value):
    return isinstance(value, int) and value > 0


def validate_player_data(player_data):
    errors = []
    if not is_valid_username(player_data.get('username')):
        errors.append('Invalid username')
    if not is_valid_email(player_data.get('email')):
        errors.append('Invalid email')
    if not is_valid_positive_integer(player_data.get('score')):
        errors.append('Score must be a positive integer')
    return errors
