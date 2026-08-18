def is_valid_username(username):
    return isinstance(username, str) and 3 <= len(username) <= 20

def is_valid_email(email):
    import re
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None

def is_valid_score(score):
    return isinstance(score, int) and 0 <= score <= 100

def is_valid_level(level):
    return isinstance(level, int) and level > 0

def is_valid_password(password):
    return isinstance(password, str) and len(password) >= 8

def is_valid_game_id(game_id):
    return isinstance(game_id, str) and len(game_id) == 36