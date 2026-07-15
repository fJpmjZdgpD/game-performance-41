import random
import math

def clamp(value, minimum, maximum):
    return max(minimum, min(value, maximum))


def random_float(min_value, max_value):
    return random.uniform(min_value, max_value)


def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def lerp(start, end, t):
    return start + (end - start) * t


def fade_in(duration, elapsed):
    if elapsed < duration:
        return elapsed / duration
    return 1.0


def fade_out(duration, elapsed):
    if elapsed < duration:
        return 1 - (elapsed / duration)
    return 0.0
