from cell import Cell
from board import Board
from cellStatus import CellStatus
import numpy as np
from copy import deepcopy
from gameStatus import GameStatus

INF = 999


class Game:
    def __init__(self):
        # height = int(input("nhap chieu cao (height): "))
        # width = int(input("nhap chieu rong (width): "))
        height, width = 3, 3
        self.board = Board(height, width)
        self.isTurnX = True
        self.winner = None

    def __checkMoveAvailable(self, board, cell):
        x = cell.posX
        y = cell.posY
        status = cell.status
        if x not in range(board.height) and y not in range(board.width):
            return False
        if board.map[x][y] != CellStatus.NONE or not self.__canFindWay(status, [], [cell]):
            return False
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i in range(board.height) and j in range(board.width) and board.map[i][j] == status:
                    return True
        return False

    def __checkAttack(self, cell):
        board = self.board
        maps = board.map
        x = cell.posX
        y = cell.posY
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i in range(0, board.height) and j in range(0, board.width) and maps[i][j] != maps[x][y] and maps[i][
                    j] != CellStatus.NONE:
                    maps[i][j] = CellStatus.BLOCK

    def __checkWin(self, board):
        maps = board.map
        maps_flat = mapFlat(maps)
        if CellStatus.X not in maps_flat:
            return GameStatus.O_WIN
        if CellStatus.O not in maps_flat:
            return GameStatus.X_WIN

        for index, cell in enumerate(maps_flat):
            if cell == CellStatus.NONE:
                x = index // self.board.width
                y = index % self.board.width
                if self.__canFindWay(CellStatus.O, [], [Cell(CellStatus.NONE, x, y)]):
                    if self.__canFindWay(CellStatus.X, [], [Cell(CellStatus.NONE, x, y)]):
                        return GameStatus.UNKNOW

        return self.__statistics()

    def __canFindWay(self, status, listCellHadCheck, queueWillCheckCell):
        cell = queueWillCheckCell.pop(0)
        listCellHadCheck.append([cell.posX, cell.posY])
        x = cell.posX
        y = cell.posY
        map = self.board.map
        width = self.board.width
        height = self.board.height

        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i in range(height) and j in range(width):
                    if map[i][j] == CellStatus.NONE and [i, j] not in listCellHadCheck:
                        queueWillCheckCell.append(Cell(map[i][j], i, j))
                    elif map[i][j] != status and (map[i][j] == CellStatus.X or map[i][j] == CellStatus.O):
                        return True

        if len(queueWillCheckCell) > 0:
            return self.__canFindWay(status, listCellHadCheck, queueWillCheckCell)
        return False

    def __statistics(self):
        maps = self.board.map
        maps_flat = mapFlat(maps)
        for index, cell in enumerate(maps_flat):
            if cell == CellStatus.NONE:
                posX = index // self.board.width
                posY = index % self.board.width
                if self.__canFindWay(CellStatus.X, [], [Cell(CellStatus.NONE, posX, posY)]):
                    maps_flat[index] = CellStatus.X
                elif self.__canFindWay(CellStatus.O, [], [Cell(CellStatus.NONE, posX, posY)]):
                    maps[posX][posY] = CellStatus.O

        point_x = maps_flat.count(CellStatus.X)
        point_o = maps_flat.count(CellStatus.O)
        if point_x == point_o:
            return GameStatus.DRAW
        return GameStatus.X_WIN if point_x > point_o else GameStatus.O_WIN

    def __move(self):
        while True:
            status = CellStatus.X if self.isTurnX else CellStatus.O
            position = input('Nhap toa do ' + str(status.value) +
                             ' (Enter "q" to end game): ')

            pos_x, pos_y = [int(x) for x in position.split()]

            cell = Cell(status, pos_x, pos_y)
            if self.__checkMoveAvailable(self.board, cell):
                self.board.setCellStatus(cell)
                if self.__checkAttack(cell):
                    pass  # todo
                self.isTurnX = not self.isTurnX
                return
            else:
                print('Please try again!')

    def __AIMove(self):
        board = self.board
        if self.__checkWin(board) != GameStatus.UNKNOW:
            return
        bestMove = None
        bestValue = INF
        for move in self.__listCanMove(board, CellStatus.O):
            currentBoard = deepcopy(board)
            currentBoard.setCellStatus(Cell(CellStatus.O, move[0], move[1]))
            moveValue = self.miniMax(currentBoard, False)
            if bestValue > moveValue:
                bestMove = move

    def miniMax(self, board, isTurnX):
        board.printBoard()

        status = CellStatus.X if isTurnX else CellStatus.O
        state = self.__checkWin(board)
        stateValue = {GameStatus.X_WIN: 10,
                      GameStatus.O_WIN: -10, GameStatus.DRAW: 0}
        if state != GameStatus.UNKNOW:
            return stateValue[state]
        listCanMove = self.__listCanMove(board, status)
        if isTurnX:
            bestValue = -INF
            for move in listCanMove:
                posX, posY = move
                board.setCellStatus(Cell(status, posX, posY))
                value = self.miniMax(board, False)
                bestValue = max(value, bestValue)
            return bestValue
        else:
            bestValue = INF
            for move in listCanMove:
                posX, posY = move
                board.setCellStatus(Cell(status, posX, posY))
                value = self.miniMax(board, True)
                bestValue = min(value, bestValue)
            return bestValue

    def __listCanMove(self, board, status):
        result = []
        maps_flat = mapFlat(board.map)
        for index, _ in enumerate(maps_flat):
            posX = index // board.width
            posY = index % board.width
            if self.__checkMoveAvailable(board, Cell(status, posX, posY)):
                result.append([posX, posY])
        return result

    def play(self):
        while True:
            self.board.printBoard()
            if self.__checkWin(self.board) != GameStatus.UNKNOW:
                break
            self.__move() if self.isTurnX else self.__AIMove()





Game().play()
