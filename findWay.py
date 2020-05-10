from cell import Cell
from cellStatus import CellStatus
from queue import Queue
from board import Board


def canFindWay(board, status, listCellHadCheck, queueWillCheckCell):
    # {posX, posY, status} = cell
    # {map, width, height} = board
    cell = queueWillCheckCell.get()
    listCellHadCheck.append([cell.posX, cell.posY])
    x = cell.posX
    y = cell.posY
    map = board.map
    width = board.width
    height = board.height

    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i in range(height) and j in range(width):
                if map[i][j] == CellStatus.NONE and [i,j] not in listCellHadCheck:
                    queueWillCheckCell.put(Cell(map[i][j], i, j))
                elif map[i][j] != status and (map[i][j] == CellStatus.X or map[i][j] == CellStatus.O):
                    return True

    if queueWillCheckCell.qsize() > 0:
        return canFindWay(board, status, listCellHadCheck, queueWillCheckCell)
    return False


# board = Board(5, 6)
# board.setCellStatus(Cell(CellStatus.TYPE_X, 0, 1))
# board.setCellStatus(Cell(CellStatus.TYPE_X, 1, 1))
# board.setCellStatus(Cell(CellStatus.TYPE_X, 1, 2))
# board.setCellStatus(Cell(CellStatus.TYPE_X, 1, 3))
# board.setCellStatus(Cell(CellStatus.TYPE_X, 1, 4))
# board.setCellStatus(Cell(CellStatus.TYPE_X, 1, 5))
# board.printBoard()

# queue = Queue()
# queue.put(Cell(, 1, 0))
# print(canFindWay(board, CellStatus.TYPE_X, [], queue))
