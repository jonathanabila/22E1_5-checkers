from constants import RED, WHITE
from models.board import Board


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

    def update(self):
        ...
