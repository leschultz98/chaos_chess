from cellStatus import CellStatus


class Cell:
    def __init__(self, status, posX, posY):
        self.status = status# if status != None else CellStatus.TYPE_NONE
        self.posX = posX
        self.posY = posY
