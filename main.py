#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Gabeitch - Платформер с монетами и врагами
Главный исполняемый файл игры
"""

import pygame
import sys
from settings import WIDTH, HEIGHT, FPS
from screens import main_menu, game_loop

# Создание окна игры (глобальные объекты для доступа из других модулей)
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gabeitch")
CLOCK = pygame.time.Clock()


def main():
    """Главная функция программы"""
    while True:
        menu_result = main_menu()

        if menu_result == "quit":
            break
        elif menu_result == "start":
            game_result = game_loop()

            while game_result == "restart":
                game_result = game_loop()

            if game_result == "quit":
                break
            # Если "menu" - возвращаемся в главное меню

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()