# pylint: disable = import-error
# pylint: disable = no-member


import sys
import pygame

from GUIs.image_source import CELL_SIZE, ImageSource
from sources.cellStatus import CellStatus

from sources.game import Game
from sources.gameStatus import GameStatus


green = (0, 255, 0) 
blue = (0, 0, 128) 

class Scene:
    def __init__(self, m, n):
        self.game = Game(m, n)
        self.board = self.game.board
        self.screen_width, self.screen_height = self.board.width * CELL_SIZE, self.board.height * CELL_SIZE
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('chaos chess')

    def draw_grid(self):
        for x in range(1, self.board.width):
            pygame.draw.line(self.screen, (0, 0, 0), (x * 100, 0), (x * 100, self.screen_height), 5)
        for x in range(1, self.board.height):
            pygame.draw.line(self.screen, (0, 0, 0), (0, x * 100), (self.screen_width, x * 100), 5)

    def draw_cell(self):
        for x in range(self.board.height):
            for y in range(self.board.width):
                if self.board.map[x][y] == CellStatus.O:
                    image = ImageSource.CELL_O.value
                elif self.board.map[x][y] == CellStatus.X:
                    image = ImageSource.CELL_X.value
                elif self.board.map[x][y] == CellStatus.BLOCK:
                    image = ImageSource.CELL_BLOCK.value
                else:
                    continue
                rect = image.get_rect()
                rect.center = (y * CELL_SIZE + 50, x * CELL_SIZE + 50)
                self.screen.blit(image, rect)

    def convert_position(self):
        x, y = pygame.mouse.get_pos()
        x = x // CELL_SIZE
        y = y // CELL_SIZE
        return (x, y)

    def draw_shadow_cursor(self):
        pygame.draw.rect(self.screen, (0, 255, 0), (
        self.convert_position()[0] * CELL_SIZE, self.convert_position()[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE), 5)

    def draw_result(self):
        font = pygame.font.SysFont('Comic Sans MS', 30)
        text = font.render(self.game.winner.value, True, green, blue) 
        textRect = text.get_rect()  
        textRect.center = self.screen.get_rect().center
        self.screen.blit(text,textRect)

    def draw(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.game.move(self.convert_position())
                    
            



            self.screen.fill((250, 250, 250))
            self.draw_grid()
            self.draw_cell()
            if self.game.winner != GameStatus.UNKNOW:
                self.draw_result()
            self.draw_shadow_cursor()
            pygame.display.flip()

# Scene(3,4).draw()