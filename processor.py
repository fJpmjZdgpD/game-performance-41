import numpy as np

class GameDataProcessor:
    def __init__(self, data):
        self.data = data

    def normalize_data(self):
        max_value = np.max(self.data)
        return self.data / max_value if max_value > 0 else self.data

    def filter_outliers(self, threshold=1.5):
        q1 = np.percentile(self.data, 25)
        q3 = np.percentile(self.data, 75)
        iqr = q3 - q1
        lower_bound = q1 - threshold * iqr
        upper_bound = q3 + threshold * iqr
        return self.data[(self.data >= lower_bound) & (self.data <= upper_bound)]

    def aggregate_scores(self):
        return np.mean(self.data)

    def process(self):
        normalized = self.normalize_data()
        filtered = self.filter_outliers()
        avg_score = self.aggregate_scores()  
        return avg_score, filtered
