import numpy as np

n = 3
type_x = 'X'
type_o = 'O'
type_block = '.'
type_none = '_'
maps = [[type_none for _ in range(n)] for _ in range(n)]
maps[0][0] = type_x
maps[n-1][n-1] = type_o
isTurnX = True

# maps[0][2] = type_o


def printBoard():
    for x in range(n):
        for y in range(n):
            print(maps[x][y], end=' ')
        print()


def check(type, x, y):
    if maps[x][y] != type_none:
        return False
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i in range(0, n) and j in range(0, n) and maps[i][j] == type:
                return True
    return False


def checkAttack(x, y):
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i in range(0, n) and j in range(0, n) and maps[i][j] != maps[x][y] and maps[i][j] != type_none:
                maps[i][j] = type_block


def move(type, x, y):
    global isTurnX
    if check(type, x, y):
        maps[x][y] = type
        checkAttack(x, y)
        isTurnX = not isTurnX
    else:
        print('Please try again!')


def checkWin():
    maps_flat = np.array(maps).flatten()
    if type_x not in maps_flat:
        print('O win!')
        return True
    if type_o not in maps_flat:
        print('X win!')
        return True
    if type_none not in maps_flat:
        print('Wait to calculate...')
        return True
    return False


while True:
    printBoard()
    if checkWin():
        break
    types = type_x if isTurnX else type_o
    pos_x, pos_y = [int(x)
                    for x in input('Nhap toa do ' + types + ': ').split()]
    move(types, pos_x, pos_y)
