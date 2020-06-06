# from GUIs.game_scene import Scene
from sources.cell import Cell
from sources.board import Board
from sources.cellStatus import CellStatus
from sources.gameStatus import GameStatus

INF = 9999


class Game:
    def __init__(self, height, width):
        # height = int(input("nhap chieu cao (height): "))
        # width = int(input("nhap chieu rong (width): "))
        self.board = Board(height, width)
        self.isTurnX = True
        self.winner = GameStatus.UNKNOW
        self.score = height + width + 1

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
                # kill het
                board.killAllEnemyNearCell(cell)
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
        # self.miniMax()
        if board.checkWin() == GameStatus.UNKNOW:
            bestValue = -INF
            for move in board.listCanMove(CellStatus.O):
                currentBoard = board.deepCopy()
                cell = Cell(CellStatus.O, move[0], move[1])
                currentBoard.setCellStatus(cell)
                currentBoard.killAllEnemyNearCell(cell)
                moveValue = self.miniMax(currentBoard, 0, True)
                if bestValue < moveValue:
                    bestValue = moveValue
                    bestMove = move

            cell = Cell(CellStatus.O, bestMove[0], bestMove[1])
            board.setCellStatus(cell)
            board.killAllEnemyNearCell(cell)

    # stupid AI board < 4x4
    def miniMax(self, board, depth, isTurnAI):
        # print("----------------------")
        # board.printBoard()
        status = CellStatus.O if isTurnAI else CellStatus.X
        state = board.checkWin()
        stateValue = {GameStatus.O_WIN: self.score - depth,
                      GameStatus.X_WIN: -self.score + depth, GameStatus.DRAW: 0}
        if state != GameStatus.UNKNOW:
            return stateValue[state]
        listCanMove = board.listCanMove(status)
        if isTurnAI:
            bestValue = INF
            for move in listCanMove:
                posX, posY = move
                cell = Cell(status, posX, posY)
                nextBoard = board.deepCopy()
                nextBoard.setCellStatus(cell)
                # warning
                nextBoard.killAllEnemyNearCell(cell)

                value = self.miniMax(nextBoard, depth + 1, False)
                bestValue = min(value, bestValue)
            return bestValue
        else:
            bestValue = -INF
            for move in listCanMove:
                posX, posY = move
                nextBoard = board.deepCopy()
                cell = Cell(status, posX, posY)
                nextBoard.setCellStatus(cell)
                # warning
                nextBoard.killAllEnemyNearCell(cell)

                value = self.miniMax(nextBoard, depth + 1, True)
                bestValue = max(value, bestValue)
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
            # Scene(self.board).draw()
