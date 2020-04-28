from cell import Cell
from board import Board
from cellStatus import CellStatus
import numpy as np


class Game:
    def __init__(self):
        self.board = Board(3, 3)
        self.isTurnX = True
        self.winner = None

    def checkMoveAvailable(self, cell):
        board = self.board
        x = cell.posX
        y = cell.posY
        if board.map[x][y] != CellStatus.TYPE_NONE:
            return False
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i in range(0, board.height) and j in range(0, board.width) and board.map[i][j] == cell.status:
                    return True
        return False

    def checkAttack(self, cell):
        board = self.board
        maps = board.map
        x = cell.posX
        y = cell.posY
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i in range(0, board.height) and j in range(0, board.width) and maps[i][j] != maps[x][y] and maps[i][j] != CellStatus.TYPE_NONE:
                    maps[i][j] = CellStatus.TYPE_BLOCK

    def checkWin(self):
        maps = self.board.map
        maps_flat = np.array(maps).flatten().tolist()
        if CellStatus.TYPE_X not in maps_flat:
            print('O win!')
            return True
        if CellStatus.TYPE_O not in maps_flat:
            print('X win!')
            return True
        return False

    def new(self):
        maps = self.board.map
        maps_flat = np.array(maps).flatten().tolist()
        point_x = maps_flat.count(CellStatus.TYPE_X)
        point_o = maps_flat.count(CellStatus.TYPE_O)
        print('\tPoint of X: ', point_x)
        print('\tPoint of Y: ', point_o)
        if point_x != point_o:
            self.winner = 'X' if point_x > point_o else 'O'
            print('\t' + self.winner + ' win!')
        else:
            print('\t~Equal~')

    def move(self, cell):
        if self.checkMoveAvailable(cell):
            self.board.map[cell.posX][cell.posY] = cell.status
            self.checkAttack(cell)
            self.isTurnX = not self.isTurnX
        else:
            print('Please try again!')

    def play(self):
        while True:
            self.board.printBoard()
            if self.checkWin():
                break
            status = CellStatus.TYPE_X if self.isTurnX else CellStatus.TYPE_O
            position = input('Nhap toa do ' + status.value +
                             ' (Enter "q" to end game): ')
            if position == 'q':
                break
            pos_x, pos_y = [int(x) for x in position.split()]
            cell = Cell(status, pos_x, pos_y)
            self.move(cell)
