class GameSettings:
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    FPS = 60
    PLAYER_SPEED = 5
    ENEMY_SPEED = 3
    MAX_ENEMIES = 10

class Colors:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

class GameStates:
    MAIN_MENU = 'main_menu'
    RUNNING = 'running'
    PAUSED = 'paused'
    GAME_OVER = 'game_over'