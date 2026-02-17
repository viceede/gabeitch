import pygame
import sys
from settings import *
from classes import Button
from utils import show_rules
from utils.sprite_sheet import ResourceLoader  # Изменено с SpriteLoader на ResourceLoader


def main_menu():
    """Главное меню игры"""
    from main import WIN, CLOCK

    # Загружаем ресурсы
    resources = ResourceLoader()
    background = resources.get_background('menu')

    menu_font = pygame.font.SysFont(None, 48)
    small_font = pygame.font.SysFont(None, 28)
    title_font = pygame.font.SysFont(None, 72)

    # Создание кнопок
    start_button = Button(WIDTH // 2 - 100, 250, 200, 50, "Начать игру")
    rules_button = Button(WIDTH // 2 - 100, 320, 200, 50, "Правила")
    quit_button = Button(WIDTH // 2 - 100, 390, 200, 50, "Выйти")

    show_rules_screen = False
    running = True

    while running:
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if show_rules_screen:
                        show_rules_screen = False
                    else:
                        running = False

        # Проверка наведения на кнопки
        if not show_rules_screen:
            start_button.check_hover(mouse_pos)
            rules_button.check_hover(mouse_pos)
            quit_button.check_hover(mouse_pos)

            # Обработка нажатий на кнопки
            if start_button.is_clicked(mouse_pos, mouse_click):
                return "start"
            if rules_button.is_clicked(mouse_pos, mouse_click):
                show_rules_screen = True
            if quit_button.is_clicked(mouse_pos, mouse_click):
                pygame.quit()
                sys.exit()

        # Отрисовка фона
        WIN.blit(background, (0, 0))

        # Полупрозрачный overlay
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        WIN.blit(overlay, (0, 0))

        # Заголовок игры
        title_text = title_font.render("Gabeitch", True, YELLOW)
        title_rect = title_text.get_rect(center=(WIDTH // 2, 80))
        WIN.blit(title_text, title_rect)

        if show_rules_screen:
            # Экран с правилами
            show_rules(WIN, small_font, 150)
        else:
            # Краткое описание под заголовком
            subtitle_text = small_font.render("Платформер с монетами и врагами", True, WHITE)
            subtitle_rect = subtitle_text.get_rect(center=(WIDTH // 2, 140))
            WIN.blit(subtitle_text, subtitle_rect)

            # Отрисовка кнопок
            start_button.draw(WIN, menu_font)
            rules_button.draw(WIN, menu_font)
            quit_button.draw(WIN, menu_font)

            # Краткие правила
            quick_rules = [
                "• Главная цель: Убить врага (прыжком сверху)",
                "• Монеты - дополнительные очки",
                "• У вас 3 жизни"
            ]
            for i, rule in enumerate(quick_rules):
                rule_text = small_font.render(rule, True, WHITE)
                WIN.blit(rule_text, (WIDTH // 2 - 150, 460 + i * 25))

        pygame.display.flip()
        CLOCK.tick(FPS)

    return "quit"