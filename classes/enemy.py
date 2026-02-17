import pygame
from settings import RED

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, left_bound, right_bound, speed=2):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.left_bound = left_bound
        self.right_bound = right_bound
        self.speed = speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.left <= self.left_bound or self.rect.right >= self.right_bound:
            self.speed *= -1