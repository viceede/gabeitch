import pygame
import sys
from settings import *
from classes import Button
from utils import show_rules
from utils.sprite_sheet import ResourceLoader


def main_menu():
    """Главное меню игры"""
    from main import WIN, CLOCK

    # Загружаем ресурсы
    resources = ResourceLoader()
    background = resources.get_background('menu')

    # Создание кнопок (чуть меньше размер)
    start_button = Button(WIDTH // 2 - 90, 240, 180, 40, "Начать игру")  # Было 200x50, стало 180x40
    rules_button = Button(WIDTH // 2 - 90, 300, 180, 40, "Правила")
    quit_button = Button(WIDTH // 2 - 90, 360, 180, 40, "Выйти")

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

        # Заголовок игры (желтым, большой)
        title_text = FONT_TITLE.render("Gabeitch", True, YELLOW)
        title_rect = title_text.get_rect(center=(WIDTH // 2, 70))  # Чуть выше
        WIN.blit(title_text, title_rect)

        if show_rules_screen:
            # Экран с правилами
            show_rules(WIN, 130)  # Начало правил чуть выше
        else:
            # Краткое описание под заголовком
            subtitle_text = FONT_MEDIUM.render("Платформер с монетами", True, WHITE)
            subtitle_rect = subtitle_text.get_rect(center=(WIDTH // 2, 120))
            WIN.blit(subtitle_text, subtitle_rect)

            subtitle_text2 = FONT_SMALL.render("и врагами", True, WHITE)
            subtitle_rect2 = subtitle_text2.get_rect(center=(WIDTH // 2, 145))
            WIN.blit(subtitle_text2, subtitle_rect2)

            # Отрисовка кнопок
            start_button.draw(WIN, FONT_MEDIUM)  # Используем MEDIUM для текста кнопок
            rules_button.draw(WIN, FONT_MEDIUM)
            quit_button.draw(WIN, FONT_MEDIUM)

            # Краткие правила под кнопками
            quick_rules = [
                "• Цель: Убить врага",
                "• Монеты - бонус",
                "• 3 жизни"
            ]
            for i, rule in enumerate(quick_rules):
                rule_text = FONT_SMALL.render(rule, True, WHITE)
                WIN.blit(rule_text, (WIDTH // 2 - 100, 420 + i * 22))  # Выше и компактнее

        pygame.display.flip()
        CLOCK.tick(FPS)

    return "quit"