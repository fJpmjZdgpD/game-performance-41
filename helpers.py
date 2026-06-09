import random
import math

def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)


def interpolate(start, end, alpha):
    return start + (end - start) * alpha


def rand_range(min_val, max_val):
    return random.uniform(min_val, max_val)


def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def random_choice(items):
    return random.choice(items)


def is_within_bounds(value, bounds):
    return bounds[0] <= value <= bounds[1]


def normalize_vector(vector):
    length = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
    return (vector[0] / length, vector[1] / length) if length > 0 else (0, 0)