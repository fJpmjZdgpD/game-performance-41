from typing import Final

# Constants for gaming performance tuning
FPS_LIMIT: Final[int] = 60
QUALITY_PRESETS: Final[dict[str, int]] = {
    'low': 720,
    'medium': 1080,
    'high': 1440,
    'ultra': 2160,
}
RESOLUTION_OPTIONS: Final[list[tuple[int, int]]] = [
    (1280, 720),
    (1920, 1080),
    (2560, 1440),
    (3840, 2160),
]

MAX_PLAYERS: Final[int] = 100
DEFAULT_VOLUME: Final[float] = 0.5

def get_quality_resolution(quality: str) -> int:
    """Get the resolution for a given quality preset.

    Args:
        quality (str): The quality preset ('low', 'medium', 'high', 'ultra').

    Returns:
        int: The resolution associated with the quality preset.
    """
    return QUALITY_PRESETS.get(quality, QUALITY_PRESETS['medium'])

def get_supported_resolutions() -> list[tuple[int, int]]:
    """Get the list of supported resolutions.

    Returns:
        list[tuple[int, int]]: The supported resolutions.
    """
    return RESOLUTION_OPTIONS
