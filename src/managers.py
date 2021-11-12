from constants import BLUE, RED, SQUARE_SIZE, WHITE
from models.board import Board

import pygame


class GameManager:
    def __init__(self, window):
        self.window = window

        self.selected_piece = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

    def _move(self, row, column):
        piece = self.board.get_piece(row, column)

        if (
            self.selected_piece is True
            and piece is None
            and (row, column) in self.valid_moves
        ):
            self.board.move(self.selected_piece, row, column)

            skipped = self.valid_moves[(row, column)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()

            return True

        return False

    def select(self, row, column):
        if self.selected_piece is True:
            result = self._move(row, column)
            if not result:
                self.selected_piece = None
                self.select(row, column)

        piece = self.board.get_piece(row, column)
        if piece is not None and piece.color == self.turn:
            self.selected_piece = piece
            self.valid_moves = self.board.get_valid_moves(self.selected_piece)
            return True

        return False

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(
                self.window,
                BLUE,
                (
                    col * SQUARE_SIZE + SQUARE_SIZE // 2,
                    row * SQUARE_SIZE + SQUARE_SIZE // 2,
                ),
                15,
            )

    def update(self):
        self.board.draw(self.window)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()
