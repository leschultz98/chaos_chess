from enum import Enum

import pygame
import os
CELL_SIZE = 100


def load(dir): return pygame.transform.scale(pygame.image.load(os.path.join('data', '../resources/'+dir)), (CELL_SIZE-5, CELL_SIZE-5))


class ImageSource(Enum):
    CELL = load('cell.png')
    CELL_BLOCK = load('cell_block.png')
    CELL_O = load('cell_o.png')
    CELL_X = load('cell_x.png')
    # CELL = pygame.transform.scale(pygame.image.load('C:/Users/lesch/PycharmProjects/chaos_chess/resources/cell.png'), (CELL_SIZE - 5, CELL_SIZE - 5))
    # CELL_BLOCK = pygame.transform.scale(pygame.image.load('C:/Users/lesch/PycharmProjects/chaos_chess/resources/cell_block.png'), (CELL_SIZE - 5, CELL_SIZE - 5))
    # CELL_O = pygame.transform.scale(pygame.image.load('C:/Users/lesch/PycharmProjects/chaos_chess/resources/cell_o.png'), (CELL_SIZE - 5, CELL_SIZE - 5))
    # CELL_X = pygame.transform.scale(pygame.image.load('C:/Users/lesch/PycharmProjects/chaos_chess/resources/cell_x.png'), (CELL_SIZE - 5, CELL_SIZE - 5))
