from enum import Enum

import pygame

CELL_SIZE = 100


def load(dir): return pygame.transform.scale(pygame.image.load(dir), (CELL_SIZE-5, CELL_SIZE-5))


class ImageSource(Enum):
    CELL = load('resources/cell.png')
    CELL_BLOCK = load('resources/cell_block.png')
    CELL_O = load('resources/cell_o.png')
    CELL_X = load('resources/cell_x.png')
