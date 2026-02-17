import pygame
from settings import *
from utils.sprite_sheet import ResourceLoader


class Tree(pygame.sprite.Sprite):
    """Класс для дерева, сквозь которое можно проходить"""

    def __init__(self, x, y):
        super().__init__()
        self.resources = ResourceLoader()

        # Загружаем текстуру дерева
        self.image = self.resources.get_object_texture('tree')

        if self.image is None:
            # Если текстура не загружена, создаем заглушку
            self.image = pygame.Surface((40, 60), pygame.SRCALPHA)
            self._create_tree_placeholder()

        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)  # Дерево стоит на платформе

        # Флаг для прохождения сквозь дерево
        self.passable = True

    def _create_tree_placeholder(self):
        """Создает заглушку для дерева, если нет текстуры"""
        # Ствол
        pygame.draw.rect(self.image, (101, 67, 33, 255), (15, 20, 10, 40))
        # Крона
        pygame.draw.circle(self.image, (34, 139, 34, 255), (20, 15), 15)
        pygame.draw.circle(self.image, (34, 139, 34, 255), (10, 10), 10)
        pygame.draw.circle(self.image, (34, 139, 34, 255), (30, 10), 10)

    def update(self):
        """Дерево не двигается, но можно добавить анимацию позже"""
        pass