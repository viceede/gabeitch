import pygame
import os

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

# --- пути к ресурсам ---
BASE_PATH = os.path.dirname(__file__)
ASSETS_PATH = os.path.join(BASE_PATH, 'assets')
SPRITES_PATH = os.path.join(ASSETS_PATH, 'sprites')
BACKGROUNDS_PATH = os.path.join(ASSETS_PATH, 'backgrounds')
FONTS_PATH = os.path.join(ASSETS_PATH, 'fonts')

# --- фоновые изображения ---
GAME_BACKGROUND = os.path.join(BACKGROUNDS_PATH, 'game_background.png')
MENU_BACKGROUND = os.path.join(BACKGROUNDS_PATH, 'menu_background.png')

# --- шрифты ---
FONT_REGULAR = os.path.join(FONTS_PATH, 'Planes_ValMore.ttf')
FONT_BOLD = os.path.join(FONTS_PATH, 'Planes_ValMore.ttf')

# Инициализация pygame
pygame.init()

# Функция для загрузки шрифта с запасным вариантом
def load_font(size, bold=False):
    """Загружает шрифт, если есть, иначе использует системный"""
    font_path = FONT_BOLD if bold else FONT_REGULAR
    try:
        if os.path.exists(font_path):
            return pygame.font.Font(font_path, size)
        else:
            print(f"Шрифт не найден: {font_path}, используется системный")
            return pygame.font.SysFont(None, size)
    except:
        return pygame.font.SysFont(None, size)

# Уменьшаем все шрифты в 1.5 раза (кроме заголовка)
# Было: 24, 32, 48, 72, 28
# Стало: 16, 22, 32, 72, 20

FONT_SMALL = load_font(16)      # Было 24 -> 16
FONT_MEDIUM = load_font(22)     # Было 32 -> 22
FONT_LARGE = load_font(32)      # Было 48 -> 32
FONT_TITLE = load_font(72, bold=True)  # Заголовок оставляем 72
FONT_HUD = load_font(20)        # Было 28 -> 20

print(f"Шрифты загружены: SMALL=16, MEDIUM=22, LARGE=32, TITLE=72, HUD=20")