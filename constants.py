FPS_TARGET = 60
MAX_PLAYERS = 100
GRAVITY = 9.81
PLAYER_SPEED = 5.0
JUMP_HEIGHT = 1.5
LEVELS = ['easy', 'medium', 'hard']
ITEMS = {'health_potion': 50, 'mana_potion': 30}
ENEMY_TYPES = ['goblin', 'orc', 'dragon']

def get_max_items():
    return sum(ITEMS.values())

def calculate_velocity(speed, time):
    return speed * time + 0.5 * GRAVITY * time ** 2

# Network settings
SERVER_IP = '192.168.1.1'
SERVER_PORT = 8080

# Game settings
DEBUG_MODE = False
MAX_FRAME_TIME = 1.0 / FPS_TARGET
