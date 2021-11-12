from typing import List

from constants import BLACK, COLS, PIECES, RED, ROWS, SQUARE_SIZE, WHITE
from models.pieces import Piece

import pygame


class Board:
    def __init__(self):
        self.board = []
        self.create_board()

        self.white_left = self.red_left = PIECES
        self.white_kings = self.red_kings = 0

    def winner(self):
        if self.red_left <= 0:
            return WHITE
        elif self.white_left <= 0:
            return RED

        return None

    def get_piece(self, row, column):
        return self.board[row][column]

    def move(self, piece: Piece, row, column):
        self.board[piece.row][piece.column], self.board[row][column] = (
            self.board[row][column],
            self.board[piece.row][piece.column],
        )

        piece.move(row, column)

        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            if piece.color == RED:
                self.red_kings += 1

    def remove(self, pieces: List[Piece]):
        for piece in pieces:
            row, column = piece.row, piece.column
            self.board[row][column] = None
            if piece is not None:
                if piece.color == RED:
                    self.red_left -= 1
                else:
                    self.white_left -= 1

    def _traverse_left(self, start, stop, step, color, left, skipped=None):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current is None:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(
                        self._traverse_left(
                            r + step, row, step, color, left - 1, skipped=last
                        )
                    )
                    moves.update(
                        self._traverse_right(
                            r + step, row, step, color, left + 1, skipped=last
                        )
                    )
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1

        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=None):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break

            current = self.board[r][right]
            if current is None:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(
                        self._traverse_left(
                            r + step, row, step, color, right - 1, skipped=last
                        )
                    )
                    moves.update(
                        self._traverse_right(
                            r + step, row, step, color, right + 1, skipped=last
                        )
                    )
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1

        return moves

    def get_valid_moves(self, piece: Piece):
        valid_moves = {}
        left, right, row = piece.column - 1, piece.column + 1, piece.row

        if piece.color == RED or piece.king:
            valid_left_move = self._traverse_left(
                row - 1, max(row - 3, -1), -1, piece.color, left
            )
            valid_right_move = self._traverse_right(
                row - 1, max(row - 3, -1), -1, piece.color, right
            )

            valid_moves.update(valid_left_move)
            valid_moves.update(valid_right_move)

        if piece.color == WHITE or piece.king:
            valid_left_move = self._traverse_left(
                row + 1, min(row + 3, ROWS), 1, piece.color, left
            )
            valid_right_move = self._traverse_right(
                row + 1, min(row + 3, ROWS), 1, piece.color, right
            )

            valid_moves.update(valid_left_move)
            valid_moves.update(valid_right_move)

        return valid_moves

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
