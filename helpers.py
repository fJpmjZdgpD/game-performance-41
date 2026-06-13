import random
import math

def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))


def random_float(min_value, max_value):
    return random.uniform(min_value, max_value)


def distance(point_a, point_b):
    return math.sqrt((point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2)


def lerp(start, end, t):
    return start + (end - start) * t


def to_radians(degrees):
    return degrees * (math.pi / 180)


def to_degrees(radians):
    return radians * (180 / math.pi)


def is_within_bounds(value, lower, upper):
    return lower <= value <= upper


def shuffle_list(items):
    random.shuffle(items)
    return items


def linear_interpolation(x0, x1, t):
    return x0 * (1 - t) + x1 * t
