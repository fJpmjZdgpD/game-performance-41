import re

def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def validate_username(username: str) -> bool:
    return len(username) >= 3 and len(username) <= 25 and username.isalnum()


def validate_password(password: str) -> bool:
    return (len(password) >= 8 and 
            any(char.isdigit() for char in password) and 
            any(char.isupper() for char in password))


def validate_age(age: int) -> bool:
    return 0 <= age <= 120


def validate_url(url: str) -> bool:
    pattern = r'^(https?:\/\/)?([\w.-]+\.[a-zA-Z]{2,}|localhost)(:[0-9]{1,5})?(\/[^\s]*)?$'
    return bool(re.match(pattern, url))