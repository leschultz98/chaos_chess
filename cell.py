from cellStatus import CellStatus


class Cell:
    def __init__(self, status, posX, posY):
        self.status = status if status != None else CellStatus.NONE
        self.posX = posX
        self.posY = posY

    def compare(self, cell):
        return self.posX == cell.posX and self.posY == cell.posY

