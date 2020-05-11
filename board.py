from cellStatus import CellStatus
from cell import Cell
from gameStatus import GameStatus

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
    
    def checkMoveAvailable(self, cell):
        height=self.height
        width=self.width
        map=self.map
        x = cell.posX
        y = cell.posY
        status = cell.status
        if x not in range(height) and y not in range(width):
            return False
        if map[x][y] != CellStatus.NONE or self.__canFindWay(status, [], [cell]) == False:
            return False
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i in range(height) and j in range(width) and map[i][j] == status:
                    return True
        return False

    def canFindWay(self, status, listCellHadCheck, queueWillCheckCell):
        # {posX, posY, status} = cell
        # {map, width, height} = board
        map = self.map
        width = self.width
        height = self.height

        cell = queueWillCheckCell.pop(0)
        listCellHadCheck.append([cell.posX, cell.posY])
        x = cell.posX
        y = cell.posY

        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i in range(height) and j in range(width):
                    if map[i][j] == CellStatus.NONE and [i, j] not in listCellHadCheck:
                        queueWillCheckCell.append(Cell(map[i][j], i, j))
                    elif map[i][j] != status and (map[i][j] == CellStatus.X or map[i][j] == CellStatus.O):
                        return True

        if len(queueWillCheckCell) > 0:
            return self.canFindWay(status, listCellHadCheck, queueWillCheckCell)
        return False

    def checkAttack(self, cell):
        map = self.map
        width = self.width
        height = self.height
        x = cell.posX
        y = cell.posY
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i in range(0, height) and j in range(0, width) and map[i][j] != map[x][y] and map[i][j] != CellStatus.NONE:
                    map[i][j] = CellStatus.BLOCK

    def checkWin(self):
        maps = board.map
        maps_flat = mapFlat(maps)
        if CellStatus.X not in maps_flat:
            return GameStatus.O_WIN
        if CellStatus.O not in maps_flat:
            return GameStatus.X_WIN
        # check
        for index, cell in enumerate(maps_flat):
            if cell == CellStatus.NONE:
                x = index // self.board.width
                y = index % self.board.width
                if self.__canFindWay(CellStatus.O, [], [Cell(CellStatus.NONE, x, y)]):
                    if self.__canFindWay(CellStatus.X, [], [Cell(CellStatus.NONE, x, y)]):
                        return GameStatus.UNKNOW

        return self.__statistics()
def mapFlat(maps): return np.array(maps).flatten().tolist()
