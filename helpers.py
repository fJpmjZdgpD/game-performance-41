import random
import math

def calculate_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

def generate_random_position(x_range, y_range):
    x = random.uniform(*x_range)
    y = random.uniform(*y_range)
    return (x, y)

def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)

def is_on_screen(position, screen_size):
    return 0 <= position[0] <= screen_size[0] and 0 <= position[1] <= screen_size[1]

def lerp(start, end, t):
    return start + (end - start) * t
