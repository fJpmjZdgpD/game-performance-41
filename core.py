import time
import numpy as np

class GameEngine:
    def __init__(self, fps):
        self.fps = fps
        self.frame_time = 1.0 / fps
        self.last_time = time.time()

    def update(self):
        current_time = time.time()
        if current_time - self.last_time >= self.frame_time:
            self.last_time = current_time
            self.process_logic()

    def process_logic(self):
        # Optimized: Process game logic here
        pass

    def run(self):
        while True:
            self.update()

if __name__ == '__main__':
    engine = GameEngine(fps=60)
    engine.run()