import sys
import pygame

from GUIs import image_source
from GUIs.image_source import CELL_SIZE
from sources.cellStatus import CellStatus
from sources.game import Game


class Scene:
    def __init__(self):
        self.game = Game(5, 3)
        self.screen_width, self.screen_height = self.game.board.width * CELL_SIZE, self.game.board.height * CELL_SIZE
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

    def draw_grid(self):
        for x in range(1, self.game.board.width):
            pygame.draw.line(self.screen, (0, 0, 0), (x * 100, 0), (x * 100, self.screen_height), 5)
        for x in range(1, self.game.board.height):
            pygame.draw.line(self.screen, (0, 0, 0), (0, x * 100), (self.screen_width, x * 100), 5)

    def draw_cell(self):
        for x in range(self.game.board.height):
            for y in range(self.game.board.width):
                if self.game.board.map[x][y] == CellStatus.O:
                    image = image_source.ImageSource.CELL_O.value
                elif self.game.board.map[x][y] == CellStatus.X:
                    image = image_source.ImageSource.CELL_X.value
                elif self.game.board.map[x][y] == CellStatus.BLOCK:
                    image = image_source.ImageSource.CELL_BLOCK.value
                else:
                    continue
                rect = image.get_rect()
                rect.center = (y * CELL_SIZE + 50, x * CELL_SIZE + 50)
                self.screen.blit(image, rect)

    def draw(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill((250, 250, 250))
            self.draw_grid()
            self.draw_cell()
            pygame.display.flip()
