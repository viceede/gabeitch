import pygame
from settings import *
from classes import Player, Platform, Enemy, Coin, Tree, Rock
from utils import show_message
from utils.sprite_sheet import ResourceLoader


def create_game_objects():
    """Создает все игровые объекты для нового запуска"""
    player = Player(100, HEIGHT - GROUND_HEIGHT - PLAYER_HEIGHT)
    player.coins_collected = 0
    player.bonus_points = 0
    player.lives = 3

    platforms = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    objects = pygame.sprite.Group()  # Группа для объектов (деревья, камни)
    all_sprites = pygame.sprite.Group()

    # земля (пол)
    ground = Platform(0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT, platform_type="ground")
    platforms.add(ground)
    all_sprites.add(ground)

    # Платформы
    level_platforms = [
        Platform(200, 340, 120, 20),
        Platform(380, 280, 120, 20),
        Platform(560, 240, 120, 20),
        Platform(350, 400, 80, 20),
    ]

    for p in level_platforms:
        platforms.add(p)
        all_sprites.add(p)

    # Дерево на второй платформе (380, 280)
    tree = Tree(400, 280)  # x=400, y=280
    objects.add(tree)
    all_sprites.add(tree)

    # Камень на третьей платформе (560, 240)
    rock = Rock(580, 240)  # x=580, y=240
    objects.add(rock)
    all_sprites.add(rock)

    # враг
    enemy = Enemy(420, HEIGHT - GROUND_HEIGHT - 40, 380, 560)
    enemies.add(enemy)
    all_sprites.add(enemy)

    # монеты
    coin_positions = [
        (230, 310),  # Монета на первой платформе
        (410, 250),  # Монета на второй платформе (рядом с деревом)
        (590, 210),  # Монета на третьей платформе (рядом с камнем)
        (380, 370),  # Монета на четвертой платформе
    ]

    for cx, cy in coin_positions:
        c = Coin(cx, cy)
        coins.add(c)
        all_sprites.add(c)

    all_sprites.add(player)

    return player, platforms, enemies, coins, objects, all_sprites


def game_loop():
    """Основной игровой цикл"""
    from main import WIN, CLOCK

    # Загружаем ресурсы
    resources = ResourceLoader()
    background = resources.get_background('game')

    player, platforms, enemies, coins, objects, all_sprites = create_game_objects()

    victory = False
    game_over = False

    running = True
    while running:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "menu"
                if event.key == pygame.K_r and (game_over or victory):
                    return "restart"

        # Обновление анимаций
        coins.update()
        objects.update()  # Обновляем объекты

        # Проверка условий победы
        if len(enemies) == 0 and not victory and player.lives > 0:
            victory = True

        if player.lives <= 0:
            game_over = True

        if game_over:
            WIN.fill(BLACK)
            show_message(WIN, "GAME OVER", RED, FONT_LARGE, -30)
            show_message(WIN, "R - рестарт | ESC - меню", WHITE, FONT_MEDIUM, 20)
            pygame.display.flip()
            continue

        if victory:
            WIN.blit(background, (0, 0))
            all_sprites.draw(WIN)

            s = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            s.fill((0, 0, 0, 128))
            WIN.blit(s, (0, 0))

            victory_text = FONT_TITLE.render("ПОБЕДА!", True, YELLOW)
            victory_rect = victory_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
            WIN.blit(victory_text, victory_rect)

            show_message(WIN, f"Монет: {player.coins_collected}", WHITE, FONT_LARGE, 20)
            show_message(WIN, "R - рестарт | ESC - меню", WHITE, FONT_MEDIUM, 50)

            pygame.display.flip()
            continue

        enemies.update()
        player.update(platforms, enemies, coins)

        WIN.blit(background, (0, 0))
        all_sprites.draw(WIN)

        # HUD
        hud_font = FONT_HUD

        coins_text = hud_font.render(f"Монеты: {player.coins_collected}", True, BLACK)
        lives_text = hud_font.render(f"Жизни: {player.lives}", True, BLACK)
        coins_left = hud_font.render(f"Ост: {len(coins)}", True, BLACK)
        enemies_left = hud_font.render(f"Враги: {len(enemies)}", True, BLACK)
        total_text = hud_font.render(f"Очки: {player.total_score}", True, BLACK)
        menu_hint = hud_font.render("ESC", True, BLACK)

        hud_bg = pygame.Surface((180, 100))
        hud_bg.set_alpha(180)
        hud_bg.fill((255, 255, 255))
        WIN.blit(hud_bg, (5, 5))

        WIN.blit(coins_text, (10, 8))
        WIN.blit(lives_text, (10, 28))
        WIN.blit(coins_left, (10, 48))
        WIN.blit(enemies_left, (10, 68))
        WIN.blit(total_text, (10, 88))

        menu_hint_bg = pygame.Surface((45, 20))
        menu_hint_bg.set_alpha(180)
        menu_hint_bg.fill((255, 255, 255))
        WIN.blit(menu_hint_bg, (WIDTH - 55, 8))
        WIN.blit(menu_hint, (WIDTH - 50, 8))

        pygame.display.flip()

    return "quit"