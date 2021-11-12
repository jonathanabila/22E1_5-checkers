from constants import BLACK, COLS, RED, ROWS, SQUARE_SIZE, WHITE
from models.pieces import Piece

import pygame


class Board:
    def __init__(self):
        self.board = []
        self.create_board()

        self.white_left = self.red_left = 12
        self.white_kings = self.red_kings = 0

    def get_piece(self, row, column):
        return self.board[row][column]

    def move(self, piece, row, column):
        self.board[piece.row][piece.col] = self.board[row][column]
        self.board[row][column] = self.board[piece.row][piece.col]

        piece.move(row, column)

        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            if piece.color == RED:
                self.red_kings += 1

    def remove(self, pieces):
        for piece in pieces:
            row, column = piece.row, piece.col
            self.board[row][column] = None
            if piece is not None:
                if piece.color == RED:
                    self.red_left -= 1
                else:
                    self.white_left -= 1

    def get_valid_moves(self, piece):
        ...

    @staticmethod
    def draw_squares(window):
        window.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(
                    window,
                    RED,
                    (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
                )

    def draw(self, window):
        self.draw_squares(window)
        for row in range(ROWS):
            for column in range(COLS):
                piece = self.board[row][column]
                if piece is not None:
                    piece.draw(window)

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for column in range(COLS):
                if column % 2 == (row + 1) % 2:
                    if row < 3:
                        piece = Piece(row, column, WHITE)
                        self.board[row].append(piece)
                    elif row > 4:
                        piece = Piece(row, column, RED)
                        self.board[row].append(piece)
                    else:
                        self.board[row].append(None)
                else:
                    self.board[row].append(None)
