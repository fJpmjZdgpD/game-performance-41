from typing import List, Tuple

def calculate_fps(frames: int, seconds: float) -> float:
    """
    Calculate frames per second (FPS).

    Parameters:
    frames (int): The number of frames rendered.
    seconds (float): The time in seconds over which the frames were rendered.

    Returns:
    float: The calculated FPS.
    """
    if seconds <= 0:
        raise ValueError("Seconds must be greater than zero.")
    return frames / seconds


def average(lst: List[float]) -> float:
    """
    Calculate the average of a list of numbers.

    Parameters:
    lst (List[float]): A list of float numbers.

    Returns:
    float: The average of the numbers in the list.
    """
    if not lst:
        raise ValueError("List must not be empty.")
    return sum(lst) / len(lst)


def get_screen_resolution() -> Tuple[int, int]:
    """
    Get the current screen resolution.

    Returns:
    Tuple[int, int]: A tuple containing the screen width and height.
    """
    import screeninfo
    monitor = screeninfo.get_monitors()[0]
    return monitor.width, monitor.height
