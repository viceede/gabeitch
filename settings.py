import pygame

# --- настройки окна ---
WIDTH, HEIGHT = 800, 480
FPS = 60

# --- цвета ---
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
GREEN = (50, 200, 50)
RED = (200, 50, 50)
YELLOW = (240, 220, 50)
BLACK = (0, 0, 0)
SKY_BLUE = (135, 206, 235)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)
ORANGE = (255, 165, 0)

# --- параметры игрока ---
PLAYER_WIDTH, PLAYER_HEIGHT = 40, 50
PLAYER_SPEED = 5
JUMP_POWER = -12
GRAVITY = 0.6

# --- платформы, монеты, враги ---
GROUND_HEIGHT = 60

# Инициализация pygame (для шрифтов)
pygame.init()
FONT_SMALL = pygame.font.SysFont(None, 28)
FONT_MEDIUM = pygame.font.SysFont(None, 36)
FONT_LARGE = pygame.font.SysFont(None, 48)
FONT_TITLE = pygame.font.SysFont(None, 72)