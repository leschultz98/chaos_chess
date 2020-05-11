from enum import Enum


class CellStatus(Enum):
    NONE = "_"
    X = "X"
    O = "O"
    BLOCK = "*"