from constants import COLS, RED, ROWS, WHITE
from models.pieces import Piece


class Board:
    def __init__(self):
        self.board = []
        self.create_board()

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
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
