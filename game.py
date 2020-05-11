from cell import Cell
from board import Board
from cellStatus import CellStatus
from copy import deepcopy
from gameStatus import GameStatus

INF = 99999


class Game:
    def __init__(self):
        # height = int(input("nhap chieu cao (height): "))
        # width = int(input("nhap chieu rong (width): "))
        height, width = 3, 3
        self.board = Board(height, width)
        self.isTurnX = True
        self.winner = GameStatus.UNKNOW

    def __move(self):
        board = self.board
        while True:
            status = CellStatus.X if self.isTurnX else CellStatus.O
            position = input('Nhap toa do ' + str(status.value) +
                             ' (Enter "q" to end game): ')

            pos_x, pos_y = [int(x) for x in position.split()]

            cell = Cell(status, pos_x, pos_y)
            if board.checkMoveAvailable(cell):
                board.setCellStatus(cell)
                # listCanAttack = board.GetListCanAttack(cell)
                # if len(listCanAttack):
                #     self.__choseKillEnemy(listCanAttack)

                return
            else:
                print('Please try again!')

    def __choseKillEnemy(self, listCanAttack):
        while True:
            position = input('Nhap toa do quan ban dich muon kill: ')
            pos_x, pos_y = [int(x) for x in position.split()]
            if [pos_x, pos_y] in listCanAttack:
                self.board.setCellStatus(Cell(CellStatus.BLOCK, pos_x, pos_y))

    def __AIMove(self):
        board = self.board

        if board.checkWin() == GameStatus.UNKNOW:
            bestValue = INF
            for move in board.listCanMove(CellStatus.O):
                currentBoard = deepcopy(board)
                currentBoard.setCellStatus(
                    Cell(CellStatus.O, move[0], move[1]))

                moveValue = self.miniMax(currentBoard, False)
                if bestValue > moveValue:
                    bestMove = move
            board.setCellStatus(Cell(CellStatus.O, bestMove[0], bestMove[1]))

    def miniMax(self, board, isTurnX):
        status = CellStatus.X if isTurnX else CellStatus.O
        state = board.checkWin()
        stateValue = {GameStatus.X_WIN: 10,
                      GameStatus.O_WIN: -10, GameStatus.DRAW: 0}
        if state != GameStatus.UNKNOW:
            return stateValue[state]
        listCanMove = board.listCanMove(status)
        if isTurnX:
            bestValue = -INF
            for move in listCanMove:
                posX, posY = move
                cell = Cell(status, posX, posY)
                nextBoard = deepcopy(board)
                nextBoard.setCellStatus(cell)
                # warning
                # listCanAttack = nextBoard.GetListCanAttack(cell)
                # if len(listCanAttack):
                #     self.__choseKillEnemy(listCanAttack)

                value = self.miniMax(nextBoard, False)
                bestValue = max(value, bestValue)
            return bestValue
        else:
            bestValue = INF
            for move in listCanMove:
                posX, posY = move
                nextBoard = deepcopy(board)
                nextBoard.setCellStatus(Cell(status, posX, posY))
                value = self.miniMax(nextBoard, True)
                bestValue = min(value, bestValue)
            return bestValue

    def play(self):
        board = self.board
        winner = self.winner
        while True:
            board.printBoard()
            winner = board.checkWin()
            if winner != GameStatus.UNKNOW:
                print(winner.value)
                break
            self.__move() if self.isTurnX else self.__AIMove()
            self.isTurnX = not self.isTurnX


Game().play()
