import pygame
from settings import WIDTH, HEIGHT, BLACK, ORANGE, DARK_GRAY


def show_message(screen, message, color, size=48, y_offset=0):
    """Отображает сообщение в центре экрана"""
    font = pygame.font.SysFont(None, size)
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
    screen.blit(text, text_rect)


def show_rules(screen, font, start_y=150):
    """Отображает правила игры"""
    rules = [
        "ПРАВИЛА ИГРЫ:",
        "1. Убейте врага, прыгнув ему на голову - это главная цель!",
        "2. Собирайте монеты для получения дополнительных очков",
        "3. У вас 3 жизни",
        "4. При касании врага сбоку или снизу - теряете жизнь",
        "",
        "ЦЕЛЬ: Убить врага (монеты - для счета)"
    ]
    for i, text in enumerate(rules):
        if i == 0:  # Заголовок
            rule_text = font.render(text, True, ORANGE)
            screen.blit(rule_text, (WIDTH // 2 - 250, start_y + i * 30))
        else:
            rule_text = font.render(text, True, BLACK)
            screen.blit(rule_text, (WIDTH // 2 - 250, start_y + i * 30))

    # Подсказка для возврата
    back_text = font.render("Нажмите ESC для возврата в меню", True, DARK_GRAY)
    back_rect = back_text.get_rect(center=(WIDTH // 2, HEIGHT - 50))
    screen.blit(back_text, back_rect)