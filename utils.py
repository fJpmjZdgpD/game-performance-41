import random

class InvalidInputError(Exception):
    pass

def calculate_score(player_moves, target_score):
    if not isinstance(player_moves, list) or not all(isinstance(move, int) for move in player_moves):
        raise InvalidInputError('player_moves must be a list of integers')
    if not isinstance(target_score, int):
        raise InvalidInputError('target_score must be an integer')
    if target_score < 0:
        raise InvalidInputError('target_score must be non-negative')

    total_score = sum(move for move in player_moves if move >= 0)
    return min(total_score, target_score)

def generate_random_moves(move_count, move_range=(1, 10)):
    if not isinstance(move_count, int) or move_count <= 0:
        raise InvalidInputError('move_count must be a positive integer')
    if not (isinstance(move_range, tuple) and len(move_range) == 2 and all(isinstance(n, int) for n in move_range)):
        raise InvalidInputError('move_range must be a tuple of two integers')
    if move_range[0] >= move_range[1]:
        raise InvalidInputError('move_range first element must be less than the second')

    return [random.randint(move_range[0], move_range[1]) for _ in range(move_count)]