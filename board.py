from cellStatus import CellStatus


class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.map = [[CellStatus.TYPE_NONE for _ in range(
            width)] for _ in range(height)]
        self.__createMap()

    def __createMap(self):
        self.map[0][0] = CellStatus.TYPE_X
        self.map[self.height-1][self.width-1] = CellStatus.TYPE_O

    def printBoard(self):
        print(" ".join([' '] + [str(x) for x in list(range(self.height))]))
        for x in range(self.height):
            print(str(x), end=' ')
            for y in range(self.width):
                print(self.map[x][y].value, end=' ')
            print()
    

