from constants import RED
from models.board import Board


class GameManager:
    def __init__(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    def select(self, row, column):
        ...

    def update(self):
        ...
