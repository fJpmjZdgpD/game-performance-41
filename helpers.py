import random
import math


def calculate_distance(point_a, point_b):
    return math.sqrt((point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2)


def random_choice(choices):
    return random.choice(choices)


def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)


def lerp(start, end, t):
    return start + (end - start) * t


def tile_position(position, tile_size):
    return (int(position[0] // tile_size[0]), int(position[1] // tile_size[1]))


def calculate_angle(point_a, point_b):
    delta_x = point_b[0] - point_a[0]
    delta_y = point_b[1] - point_a[1]
    return math.degrees(math.atan2(delta_y, delta_x))