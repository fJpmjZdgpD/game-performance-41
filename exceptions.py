class GameError(Exception):
    pass

class InvalidInputError(GameError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ResourceNotFoundError(GameError):
    def __init__(self, resource):
        self.resource = resource
        self.message = f'Resource not found: {self.resource}'
        super().__init__(self.message)

class NotAuthorizedError(GameError):
    def __init__(self, action):
        self.action = action
        self.message = f'Not authorized to perform action: {self.action}'
        super().__init__(self.message)

class GameStateError(GameError):
    def __init__(self, state):
        self.state = state
        self.message = f'Invalid game state: {self.state}'
        super().__init__(self.message)
