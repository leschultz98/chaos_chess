from cellStatus import CellStatus
from cell import Cell


class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.map = [[CellStatus.NONE for _ in range(
            width)] for _ in range(height)]
        self.__createMap()

    def __createMap(self):
        self.map[0][0] = CellStatus.X
        self.map[self.height - 1][self.width - 1] = CellStatus.O

    def printBoard(self):
        print(" ".join([' '] + [str(x) for x in list(range(self.width))]))
        for x in range(self.height):
            print(str(x), end=' ')
            for y in range(self.width):
                print(self.map[x][y].value, end=' ')
            print()

    def setCellStatus(self, cell):
        self.map[cell.posX][cell.posY] = cell.status
