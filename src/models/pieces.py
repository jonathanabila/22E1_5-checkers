from constants import CROWN, GREY, SQUARE_SIZE

import pygame.draw

PADDING = 15
OUTLINE = 2


class Piece:
    def __init__(self, row, column, color):
        self.row = row
        self.column = column
        self.color = color

        self._king = False

        self.x = 0
        self.y = 0

        self._calculate_position()

    def __repr__(self):
        return f"color: {self.color}"

    @property
    def king(self):
        return self._king

    def _calculate_position(self):
        self.x = SQUARE_SIZE * self.column + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self._king = True

    def move(self, row, column):
        self.row = row
        self.column = column
        self._calculate_position()

    def draw(self, window):
        radius = SQUARE_SIZE // 2 - PADDING
        pygame.draw.circle(window, GREY, (self.x, self.y), radius + OUTLINE)
        pygame.draw.circle(window, self.color, (self.x, self.y), radius)

        if self.king is True:
            window.blit(
                CROWN,
                (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2),
            )
