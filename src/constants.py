import pygame

# Dimensions
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 10, 10

SQUARE_SIZE = WIDTH // COLS


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

# Assets
crown_size = (44, 25)
crown_image = pygame.image.load("assets/crown.png")
CROWN = pygame.transform.scale(crown_image, crown_size)
