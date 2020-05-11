from cell import Cell
from board import Board
from cellStatus import CellStatus
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
       

    

    def __move(self):
        board=self.board
        while True:
            status = CellStatus.X if self.isTurnX else CellStatus.O
            position = input('Nhap toa do ' + str(status.value) +
                             ' (Enter "q" to end game): ')

            pos_x, pos_y = [int(x) for x in position.split()]

            cell = Cell(status, pos_x, pos_y)
            if board.checkMoveAvailable(cell):
                board.setCellStatus(cell)
                if board.checkAttack(cell):
                    pass  # todo
                self.isTurnX = not self.isTurnX
                return
            else:
                print('Please try again!')

    def __AIMove(self):
        board = self.board
        if board.checkWin() != GameStatus.UNKNOW:
            return
        bestMove = None
        bestValue = INF
        for move in board.listCanMove(CellStatus.O):
            currentBoard = deepcopy(board)
            currentBoard.setCellStatus(Cell(CellStatus.O, move[0], move[1]))
            moveValue = self.miniMax(currentBoard, False)
            if bestValue > moveValue:
                bestMove = move

    def miniMax(self, board, isTurnX):
        board.printBoard()

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

    def play(self):
        board=self.board
        while True:
            board.printBoard()
            if board.checkWin() != GameStatus.UNKNOW:
                break
            self.__move() if self.isTurnX else self.__AIMove()





Game().play()
