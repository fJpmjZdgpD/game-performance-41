import re

def is_valid_username(username):
    return bool(re.match(r'^[a-zA-Z0-9_]{3,20}$', username))


def is_valid_password(password):
    return (len(password) >= 8 and 
            any(c.isdigit() for c in password) and 
            any(c.isupper() for c in password) and 
            any(c.islower() for c in password))


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))


def validate_user(credentials):
    username = credentials.get('username')
    password = credentials.get('password')
    email = credentials.get('email')
    if not is_valid_username(username):
        return 'Invalid username'
    if not is_valid_password(password):
        return 'Invalid password'
    if not is_valid_email(email):
        return 'Invalid email'
    return 'Valid credentials'