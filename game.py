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
            position = input('Nhap toa do ' + status.value +
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

    def stop(self):
        pass





Game().play()
