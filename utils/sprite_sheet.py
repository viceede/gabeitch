import os
import pygame
from settings import *


class ResourceLoader:
    """Класс для загрузки и хранения всех ресурсов (спрайты и фоны)"""

    _instance = None
    _sprites = {}
    _backgrounds = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load_all_resources()
        return cls._instance

    def _load_all_resources(self):
        """Загружает все ресурсы из папки assets"""
        self._load_all_sprites()
        self._load_all_backgrounds()

    def _load_all_sprites(self):
        """Загружает все спрайты"""
        # Загрузка спрайтов игрока
        player_path = os.path.join(SPRITES_PATH, 'player')
        self._sprites['player'] = {
            'idle': self._load_animation(player_path, 'player_idle', 2),
            'walk': self._load_animation(player_path, 'player_walk', 4),
            'jump': self._load_image(os.path.join(player_path, 'player_jump.png')),
            'fall': self._load_image(os.path.join(player_path, 'player_fall.png'))
        }

        # Загрузка спрайтов врага
        enemy_path = os.path.join(SPRITES_PATH, 'enemy')
        self._sprites['enemy'] = {
            'idle': self._load_animation(enemy_path, 'enemy_idle', 2),
            'walk': self._load_animation(enemy_path, 'enemy_walk', 2)
        }

        # Загрузка спрайтов монет
        coin_path = os.path.join(SPRITES_PATH, 'coin')
        self._sprites['coin'] = self._load_animation(coin_path, 'coin', 4)

    def _load_all_backgrounds(self):
        """Загружает все фоновые изображения"""
        # Фон для игры
        self._backgrounds['game'] = self._load_image(GAME_BACKGROUND, (WIDTH, HEIGHT))

        # Фон для меню (опционально)
        if os.path.exists(MENU_BACKGROUND):
            self._backgrounds['menu'] = self._load_image(MENU_BACKGROUND, (WIDTH, HEIGHT))
        else:
            # Если нет фона для меню, используем игровой фон
            self._backgrounds['menu'] = self._backgrounds['game']

    def _load_image(self, path, scale=None):
        """Загружает одно изображение"""
        try:
            if os.path.exists(path):
                image = pygame.image.load(path).convert_alpha()
            else:
                # Если файл не найден, создаем цветную заглушку
                print(f"Предупреждение: Не удалось загрузить {path}")
                image = pygame.Surface((WIDTH, HEIGHT))
                image.fill(SKY_BLUE)
                return image
        except pygame.error:
            print(f"Предупреждение: Ошибка загрузки {path}")
            image = pygame.Surface((WIDTH, HEIGHT))
            image.fill(SKY_BLUE)
            return image

        if scale:
            image = pygame.transform.scale(image, scale)
        return image

    def _load_animation(self, folder, base_name, count, scale=None):
        """Загружает анимацию из нескольких файлов"""
        frames = []
        for i in range(1, count + 1):
            path = os.path.join(folder, f"{base_name}_{i}.png")
            frame = self._load_image(path, scale)
            frames.append(frame)

        # Если ни один кадр не загрузился, создаем заглушку
        if not frames:
            surf = pygame.Surface((40, 40))
            surf.fill(RED)
            frames = [surf]

        return frames

    def get_player_animation(self, state):
        """Возвращает анимацию игрока для указанного состояния"""
        return self._sprites['player'].get(state, [self._sprites['player']['idle'][0]])

    def get_enemy_animation(self, state):
        """Возвращает анимацию врага для указанного состояния"""
        return self._sprites['enemy'].get(state, [self._sprites['enemy']['idle'][0]])

    def get_coin_animation(self):
        """Возвращает анимацию монеты"""
        return self._sprites['coin']

    def get_background(self, name='game'):
        """Возвращает фоновое изображение"""
        return self._backgrounds.get(name, self._backgrounds['game'])