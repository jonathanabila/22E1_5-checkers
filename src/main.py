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

        if game.get_winner() is not None:
            print(f"The game finished with: '{game.get_winner()}' as winner!")
            run = False

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row, col = get_mouse_position(pos)
            game.select(row, col)

        game.update()

    pygame.quit()


if __name__ == "__main__":
    main()
