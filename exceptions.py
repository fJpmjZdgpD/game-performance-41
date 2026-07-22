class GameError(Exception):
    pass

class InvalidInputError(GameError):
    def __init__(self, message="Invalid input provided."):
        self.message = message
        super().__init__(self.message)

class ConnectionError(GameError):
    def __init__(self, message="Failed to connect to the game server."):
        self.message = message
        super().__init__(self.message)

class ResourceNotFoundError(GameError):
    def __init__(self, resource_name):
        self.message = f'Resource not found: {resource_name}'
        super().__init__(self.message)

class TimeoutError(GameError):
    def __init__(self, message="The operation has timed out."):
        self.message = message
        super().__init__(self.message)
