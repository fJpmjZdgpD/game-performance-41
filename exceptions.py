class GameError(Exception):
    """Base class for exceptions in this game."""

class AssetLoadError(GameError):
    """Exception raised for errors in asset loading."""

class InvalidInputError(GameError):
    """Exception raised for invalid user input."""

class GameStateError(GameError):
    """Exception raised for errors related to game state."""

class ConfigurationError(GameError):
    """Exception raised for configuration errors."""

def handle_error(error):
    if isinstance(error, AssetLoadError):
        return {"error": "Failed to load game assets."}
    elif isinstance(error, InvalidInputError):
        return {"error": "Invalid input provided by user."}
    elif isinstance(error, GameStateError):
        return {"error": "Game state is invalid or corrupted."}
    elif isinstance(error, ConfigurationError):
        return {"error": "Invalid configuration settings detected."}
    return {"error": "An unknown error occurred."}