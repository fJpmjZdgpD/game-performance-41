import numpy as np

class GamePerformance:
    def __init__(self, frame_data):
        self.frame_data = np.array(frame_data)
        self.optimized_data = None

    def optimize_frame_data(self):
        self.optimized_data = np.mean(self.frame_data, axis=0)

    def get_average_fps(self):
        return 1 / np.mean(self.optimized_data) if self.optimized_data is not None else 0

    def analyze_performance(self):
        self.optimize_frame_data()
        average_fps = self.get_average_fps()
        return average_fps

# Example usage:
# performance = GamePerformance(frame_data)
# print(performance.analyze_performance())