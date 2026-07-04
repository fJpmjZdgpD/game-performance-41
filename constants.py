FPS_LIMIT = 60
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
ASPECT_RATIO = SCREEN_WIDTH / SCREEN_HEIGHT
PLAYER_SPEED = 5
ENEMY_SPEED = 3
GRAVITY = 9.81
JUMP_HEIGHT = 10
LEVELS = {
    1: {'name': 'Forest', 'difficulty': 1},
    2: {'name': 'Desert', 'difficulty': 2},
    3: {'name': 'Mountain', 'difficulty': 3}
}
COLORS = {
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0),
    'RED': (255, 0, 0),
    'GREEN': (0, 255, 0),
    'BLUE': (0, 0, 255)
}
SOUNDS = {
    'jump': 'assets/sounds/jump.wav',
    'explosion': 'assets/sounds/explosion.wav',
    'game_over': 'assets/sounds/game_over.wav'
}