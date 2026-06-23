import numpy as np

class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.entities = []
        self.running = True

    def add_entity(self, entity):
        self.entities.append(entity)

    def run(self):
        while self.running:
            self.update_entities()
            self.render()

    def update_entities(self):
        for entity in self.entities:
            entity.update()

    def render(self):
        frame = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        for entity in self.entities:
            position = entity.get_position()
            frame[position[1]:position[1]+entity.height,
                  position[0]:position[0]+entity.width] += entity.color
        self.display_frame(frame)

    def display_frame(self, frame):
        # Placeholder for display implementation
        pass

class Entity:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def update(self):
        # Update entity logic
        pass

    def get_position(self):
        return (self.x, self.y)

engine = GameEngine(800, 600)
engine.run()