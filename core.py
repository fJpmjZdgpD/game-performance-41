import time

class GameEngine:
    def __init__(self):
        self.entities = []
        self.running = False

    def add_entity(self, entity):
        self.entities.append(entity)

    def start(self):
        self.running = True
        self.loop()

    def loop(self):
        last_time = time.time()
        while self.running:
            current_time = time.time()
            delta_time = current_time - last_time
            last_time = current_time
            self.update(delta_time)
            self.render()

    def update(self, delta_time):
        for entity in self.entities:
            entity.update(delta_time)

    def render(self):
        for entity in self.entities:
            entity.render()

    def stop(self):
        self.running = False

class GameEntity:
    def __init__(self, name):
        self.name = name

    def update(self, delta_time):
        pass

    def render(self):
        pass
