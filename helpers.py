import random
import numpy as np

def generate_random_position(max_x, max_y):
    return (random.randint(0, max_x), random.randint(0, max_y))


def calculate_distance(point1, point2):
    return np.linalg.norm(np.array(point1) - np.array(point2))


def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))


def lerp(start, end, t):
    return start + (end - start) * t


def is_power_of_two(n):
    return (n & (n - 1)) == 0 and n > 0


def load_image(image_path):
    from PIL import Image
    return Image.open(image_path)


def save_image(image, path):
    image.save(path)