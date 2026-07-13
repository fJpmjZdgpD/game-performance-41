import random
import numpy as np

def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)


def random_choice(choices):
    return random.choice(choices)


def lerp(start, end, t):
    return start + (end - start) * t


def distance(point_a, point_b):
    return np.linalg.norm(np.array(point_a) - np.array(point_b))


def is_power_of_two(n):
    return (n != 0) and (n & (n - 1)) == 0


def interpolate_colors(color_a, color_b, t):
    return tuple(clamp(int(a + (b - a) * t), 0, 255) for a, b in zip(color_a, color_b))


def degrees_to_radians(degrees):
    return degrees * (np.pi / 180)


def radians_to_degrees(radians):
    return radians * (180 / np.pi)
