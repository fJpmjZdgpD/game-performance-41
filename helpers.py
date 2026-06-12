import random

class GameHelpers:
    @staticmethod
    def random_choice(choices):
        return random.choice(choices)

    @staticmethod
    def calculate_distance(pos1, pos2):
        return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5

    @staticmethod
    def clamp(value, min_value, max_value):
        return max(min_value, min(value, max_value))

    @staticmethod
    def lerp(start, end, t):
        return start + (end - start) * t

    @staticmethod
    def get_random_int(min_value, max_value):
        return random.randint(min_value, max_value)

    @staticmethod
    def split_string(text, delimiter=' '):
        return text.split(delimiter)