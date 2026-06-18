def calculate_fps(frames, elapsed_time):
    if elapsed_time > 0:
        return frames / elapsed_time
    return 0


def lerp(start, end, t):
    return start + (end - start) * t


def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))


def load_image(image_path):
    import pygame
    image = pygame.image.load(image_path)
    return image.convert_alpha()


def rotate_image(image, angle):
    import pygame
    return pygame.transform.rotate(image, angle)


def distance(point_a, point_b):
    import math
    return math.sqrt((point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2)


def truncate(value, decimal_places):
    factor = 10 ** decimal_places
    return int(value * factor) / factor


def sign(value):
    return (value > 0) - (value < 0)