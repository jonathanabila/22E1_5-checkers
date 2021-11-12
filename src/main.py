from constants import FPS, HEIGHT, SQUARE_SIZE, WIDTH
from managers import GameManager

import pygame

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")


def get_mouse_position(position):
    x, y = position
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    game = GameManager(WINDOW)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                row, column = get_mouse_position(position)
                game.select(row, column)

        game.update()

    pygame.quit()


if __name__ == "__main__":
    main()
