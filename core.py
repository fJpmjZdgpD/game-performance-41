import time
import os

class Game:
    def __init__(self, name):
        self.name = name
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.time()

    def end(self):
        self.end_time = time.time()

    def get_duration(self):
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        return 0

def optimize_loading(resources):
    return {key: load_resource(key) for key in resources}

def load_resource(key):
    path = os.path.join('assets', key)
    with open(path, 'rb') as file:
        return file.read()

class ResourceManager:
    def __init__(self, resources):
        self.resources = optimize_loading(resources)

    def get_resource(self, key):
        return self.resources.get(key)