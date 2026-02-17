import pygame
from settings import WIDTH, HEIGHT, WHITE, ORANGE
from settings import FONT_SMALL, FONT_MEDIUM, FONT_LARGE, FONT_TITLE


def show_message(screen, message, color, font=None, y_offset=0):
    """Отображает сообщение в центре экрана"""
    if font is None:
        font = FONT_MEDIUM
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
    screen.blit(text, text_rect)


def show_rules(screen, start_y=140):  # Уменьшил start_y
    """Отображает правила игры белым цветом"""
    rules = [
        "ПРАВИЛА ИГРЫ:",
        "1. Убейте врага, прыгнув ему на голову",
        "2. Собирайте монеты для очков",
        "3. У вас 3 жизни",
        "4. При касании врага сбоку - жизнь отнимается",
        "",
        "ЦЕЛЬ: Убить врага"
    ]

    # Заголовок оранжевым
    title_text = FONT_LARGE.render(rules[0], True, ORANGE)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, start_y))

    # Остальные правила белым (уменьшил интервал между строками)
    for i, text in enumerate(rules[1:], 1):
        rule_text = FONT_MEDIUM.render(text, True, WHITE)
        screen.blit(rule_text, (WIDTH // 2 - 220, start_y + i * 28))  # Было 35, стало 28

    # Подсказка для возврата
    back_text = FONT_SMALL.render("ESC - назад", True, WHITE)
    back_rect = back_text.get_rect(center=(WIDTH // 2, HEIGHT - 40))
    screen.blit(back_text, back_rect)