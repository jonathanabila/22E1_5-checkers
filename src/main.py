from agents import minimax
from constants import FPS, HEIGHT, SQUARE_SIZE, WIDTH
from managers import GameManager

import pygame

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")

MAXIMUM_DEPTH = 4


def get_mouse_position(position):
    x, y = position
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    run = True
    end = False

    clock = pygame.time.Clock()
    game = GameManager(WINDOW)

    while run:
        clock.tick(FPS if not end else 0)

        if game.get_winner() is not None:
            end = True

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            run = False

        if end:
            continue

        if game.is_ai_turn():
            _, new_board = minimax(game, MAXIMUM_DEPTH, True, game.white_player)

            if new_board == game.board:
                # There are no available moves to be done.
                end = True

            game.select_ai_move(new_board)

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row, col = get_mouse_position(pos)
            game.select(row, col)

        game.update()

    pygame.quit()


if __name__ == "__main__":
    main()
