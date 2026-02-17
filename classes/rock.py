import pygame
from settings import *
from utils.sprite_sheet import ResourceLoader


class Rock(pygame.sprite.Sprite):
    """Класс для камня, сквозь который можно проходить"""

    def __init__(self, x, y):
        super().__init__()
        self.resources = ResourceLoader()

        # Загружаем текстуру камня
        self.image = self.resources.get_object_texture('rock')

        if self.image is None:
            # Если текстура не загружена, создаем заглушку
            self.image = pygame.Surface((40, 30), pygame.SRCALPHA)
            self._create_rock_placeholder()

        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)  # Камень стоит на платформе

        # Флаг для прохождения сквозь камень
        self.passable = True

    def _create_rock_placeholder(self):
        """Создает заглушку для камня, если нет текстуры"""
        # Основная форма камня
        rock_color = (128, 128, 128, 255)  # Серый
        dark_color = (80, 80, 80, 255)  # Темно-серый
        light_color = (160, 160, 160, 255)  # Светло-серый

        # Рисуем камень овальной формы
        pygame.draw.ellipse(self.image, rock_color, (5, 5, 30, 20))

        # Добавляем детали текстуры
        pygame.draw.ellipse(self.image, dark_color, (10, 8, 8, 8))
        pygame.draw.ellipse(self.image, dark_color, (22, 10, 6, 6))
        pygame.draw.ellipse(self.image, light_color, (15, 12, 5, 5))

        # Добавляем тени для объема
        pygame.draw.line(self.image, dark_color, (8, 18), (15, 20), 2)
        pygame.draw.line(self.image, light_color, (25, 12), (30, 15), 2)

    def update(self):
        """Камень не двигается"""
        pass