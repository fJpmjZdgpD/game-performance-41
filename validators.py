import re

def is_valid_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

def is_valid_username(username):
    return 3 <= len(username) <= 20 and username.isalnum()

def is_valid_score(score):
    return isinstance(score, (int, float)) and 0 <= score <= 100

def is_non_empty_string(s):
    return isinstance(s, str) and bool(s.strip())

def is_valid_game_id(game_id):
    return isinstance(game_id, int) and game_id > 0

if __name__ == '__main__':
    print(is_valid_email('test@example.com'))  # True
    print(is_valid_username('user1'))  # True
    print(is_valid_score(85.5))  # True
    print(is_non_empty_string(' Hello '))  # True
    print(is_valid_game_id(1))  # True