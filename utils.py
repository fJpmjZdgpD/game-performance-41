import numpy as np


def calculate_distance(point_a, point_b):
    return np.linalg.norm(np.array(point_a) - np.array(point_b))


def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)


def interpolate(value_a, value_b, t):
    return (1 - t) * value_a + t * value_b


def lerp(start, end, fraction):
    return start + (end - start) * fraction


def is_power_of_two(number):
    return (number != 0) and (number & (number - 1)) == 0


def random_choice(sequence):
    return np.random.choice(sequence)


def create_vector(x, y, z):
    return np.array([x, y, z])


def distance_squared(point_a, point_b):
    return (point_a[0] - point_b[0]) ** 2 + (point_a[1] - point_b[1]) ** 2 + (point_a[2] - point_b[2]) ** 2


def normalize(vector):
    norm = np.linalg.norm(vector)
    return vector / norm if norm > 0 else vector
