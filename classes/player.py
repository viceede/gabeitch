import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False
        self.lives = 3
        self.coins_collected = 0  # Только монеты
        self.bonus_points = 0      # Бонусные очки за убийство врагов
        self.start_x = x
        self.start_y = y

    @property
    def total_score(self):
        """Общий счет = монеты + бонусы"""
        return self.coins_collected + self.bonus_points

    def handle_input(self, keys):
        self.vel_x = 0
        # Управление на WASD
        if keys[pygame.K_a]:  # Влево
            self.vel_x = -PLAYER_SPEED
        if keys[pygame.K_d]:  # Вправо
            self.vel_x = PLAYER_SPEED
        # Прыжок на пробел или W
        if (keys[pygame.K_SPACE] or keys[pygame.K_w]) and self.on_ground:
            self.vel_y = JUMP_POWER
            self.on_ground = False

    def apply_gravity(self):
        self.vel_y += GRAVITY
        if self.vel_y > 15:
            self.vel_y = 15

    def update(self, platforms, enemies, coins):
        keys = pygame.key.get_pressed()
        self.handle_input(keys)
        self.apply_gravity()

        # движение по X
        self.rect.x += self.vel_x
        self.collide_x(platforms)

        # проверка выхода за левую и правую границы карты
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH

        # движение по Y
        self.rect.y += self.vel_y
        self.on_ground = False
        self.collide_y(platforms)

        # проверка выхода за верхнюю границу
        if self.rect.top < 0:
            self.rect.top = 0
            self.vel_y = 0

        # столкновения с врагами
        enemy_hit_list = pygame.sprite.spritecollide(self, enemies, False)
        for enemy in enemy_hit_list:
            # если сверху — убиваем врага
            if self.vel_y > 0 and self.rect.bottom <= enemy.rect.centery + 10:
                enemy.kill()
                self.vel_y = JUMP_POWER / 1.5
                self.bonus_points += 5  # Бонус за убийство врага (отдельно)
            else:
                # иначе теряем жизнь и откатываемся
                self.lives -= 1
                self.rect.topleft = (self.start_x, self.start_y)
                self.vel_y = 0

        # сбор монет
        coin_hit_list = pygame.sprite.spritecollide(self, coins, True)
        for _ in coin_hit_list:
            self.coins_collected += 1  # Только монеты

    def collide_x(self, platforms):
        for p in platforms:
            if self.rect.colliderect(p.rect):
                if self.vel_x > 0:
                    self.rect.right = p.rect.left
                elif self.vel_x < 0:
                    self.rect.left = p.rect.right

    def collide_y(self, platforms):
        for p in platforms:
            if self.rect.colliderect(p.rect):
                if self.vel_y > 0:
                    self.rect.bottom = p.rect.top
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0:
                    self.rect.top = p.rect.bottom
                    self.vel_y = 0