from enum import Enum, auto


class GameStatus(Enum):
    DRAW = "DRAW"
    X_WIN = "OMG X WIN"
    O_WIN = "O WIN"
    UNKNOW = auto()
