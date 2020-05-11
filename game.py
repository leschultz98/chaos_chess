from cell import Cell
from board import Board
from cellStatus import CellStatus
import numpy as np
from queue import Queue
from copy import deepcopy
from gameStatus import GameStatus


class Game:
    def __init__(self):
        height = input("nhap chieu cao (height): ")
        width = input("nhap chieu rong (width): ")

        self.board = Board(height, width)
        self.isTurnX = True
        self.winner = None

    def __checkMoveAvailable(self, cell):
        board = self.board
        x = cell.posX
        y = cell.posY
        queue = Queue()
        queue.put(cell)
        status = CellStatus.X if self.isTurnX else CellStatus.O
        if board.map[x][y] != CellStatus.NONE or self.__canFindWay(status, [], queue) == False:
            return False
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i in range(board.height) and j in range(board.width) and board.map[i][j] == cell.status:
                    return True
        return False

    def __checkAttack(self, cell):
        board = self.board
        maps = board.map
        x = cell.posX
        y = cell.posY
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i in range(0, board.height) and j in range(0, board.width) and maps[i][j] != maps[x][y] and maps[i][j] != CellStatus.NONE:
                    maps[i][j] = CellStatus.BLOCK

    def __checkWin(self):
        maps = self.board.map
        maps_flat = np.array(maps).flatten().tolist()
        if CellStatus.X not in maps_flat:
            return GameStatus.O_WIN
        if CellStatus.O not in maps_flat:
            return GameStatus.X_WIN
        # check
        for index, cell in enumerate(maps_flat):
            if cell == CellStatus.NONE:
                x = index / self.board.width
                y = index % self.board.width
                queue = Queue()
                queue.put(Cell(CellStatus.NONE, x, y))
                if (self.__canFindWay(CellStatus.O, [], queue) == True and self.__canFindWay(CellStatus.X, [], queue) == True):
                    return GameStatus.UNKNOW

        return self.__statistics()

    def __canFindWay(self, status, listCellHadCheck, queueWillCheckCell):
        # {posX, posY, status} = cell
        # {map, width, height} = board

        cell = queueWillCheckCell.get()
        listCellHadCheck.append([cell.posX, cell.posY])
        x = cell.posX
        y = cell.posY
        map = self.board.map
        width = self.board.width
        height = self.board.height

        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i in range(height) and j in range(width):
                    if map[i][j] == CellStatus.NONE and [i, j] not in listCellHadCheck:
                        queueWillCheckCell.put(Cell(map[i][j], i, j))
                    elif map[i][j] != status and (map[i][j] == CellStatus.X or map[i][j] == CellStatus.O):
                        return True

        if queueWillCheckCell.qsize() > 0:
            return self.__canFindWay(status, listCellHadCheck, queueWillCheckCell)
        return False

    def __statistics(self):
        maps = self.board.map
        maps_flat = np.array(maps).flatten().tolist()
        for index, cell in enumerate(maps_flat):
            if cell == CellStatus.NONE:
                x = index / self.board.width
                y = index % self.board.width
                if self.__canFindWay(CellStatus.X, [], Queue()):
                    maps_flat[index] = CellStatus.X
                elif self.__canFindWay(CellStatus.O, [], Queue()):
                    maps[x][y] = CellStatus.O

        point_x = maps_flat.count(CellStatus.X)
        point_o = maps_flat.count(CellStatus.O)
        if point_x == point_o:
            return GameStatus.DRAW
        return GameStatus.X_WIN if point_x > point_o else GameStatus.O_WIN

    def __move(self, cell):
        if self.__checkMoveAvailable(cell):
            self.board.setCellStatus(cell)
            if self.__checkAttack(cell):
                pass  # todo
            self.isTurnX = not self.isTurnX
        else:
            print('Please try again!')

    def __AIMove(self):
        if self.__checkWin() != GameStatus.UNKNOW:
            return
        status = CellStatus.O

        maps = self.board.map

        self.maxmin()

    def maxmin(self):
        pass

    def play(self):
        while True:
            self.board.printBoard()
            if self.__checkWin():
                break
            status = CellStatus.X if self.isTurnX else CellStatus.O
            position = input('Nhap toa do ' + status.value +
                             ' (Enter "q" to end game): ')
            if position == 'q':
                break
            pos_x, pos_y = [int(x) for x in position.split()]
            cell = Cell(status, pos_x, pos_y)
            self.__move(cell)

    def stop(self):
        pass
