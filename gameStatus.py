from enum import Enum, auto


class GameStatus(Enum):
    DRAW = auto()
    X_WIN = auto()
    O_WIN = auto()
    UNKNOW = auto()
