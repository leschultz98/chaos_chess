from enum import Enum
import os
import pygame

CELL_STEP = 20


def load(dir): return pygame.transform.scale(pygame.image.load(
    os.path.join('data', '../resources/'+dir)), (CELL_STEP, CELL_STEP))


class ImangeSource(Enum):
    CELL = load('cell.png')
    CELL_CLICK = load('cell_click.png')
    CELL_X = load('cell_x.png')
    CELL_X_CLICK = load('cell_x_click.png')
    CELL_O = load('cell_o.png')
    CELL_O_CLICK = load('cell_o_click.png')
    CELL_BLOCK = load('cell_block.png')
    CELL_BLOCK_CLICK = load('cell_block_click.png')
