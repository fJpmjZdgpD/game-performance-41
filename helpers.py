import numpy as np

def normalize_array(arr):
    return (arr - np.min(arr)) / (np.max(arr) - np.min(arr)) if np.max(arr) - np.min(arr) != 0 else arr


def average_score(scores):
    return np.mean(scores)


def filter_high_scores(scores, threshold):
    return [score for score in scores if score > threshold]


def sort_scores(scores):
    return sorted(scores, reverse=True)


def convert_to_percentage(score, total):
    return (score / total) * 100 if total > 0 else 0


def is_valid_score(score):
    return 0 <= score <= 100