import random
import numpy as np

def clamp(value, minimum, maximum):
    return max(minimum, min(value, maximum))


def lerp(start, end, t):
    return start + (end - start) * t


def random_choice(choices):
    return random.choice(choices)


def calculate_distance(point1, point2):
    return np.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def normalize_vector(vector):
    magnitude = np.sqrt(sum(coord ** 2 for coord in vector))
    return [coord / magnitude for coord in vector] if magnitude else vector


def average(lst):
    return sum(lst) / len(lst) if lst else 0


def shuffle_list(lst):
    random.shuffle(lst)
    return lst
