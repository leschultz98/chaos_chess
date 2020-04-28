import numpy as np

n = 5
type_x = 'X'
type_o = 'O'
type_block = '.'
type_none = '_'
maps = [[type_none for _ in range(n)] for _ in range(n)]
maps[0][0] = type_x
maps[n-1][n-1] = type_o
isTurnX = True


def printBoard():
    print(" ".join([' '] + [str(x) for x in list(range(n))]))
    for x in range(n):
        print(str(x), end=' ')
        for y in range(n):
            print(maps[x][y], end=' ')
        print()


def checkMoveAvailable(type, x, y):
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
    if checkMoveAvailable(type, x, y):
        maps[x][y] = type
        checkAttack(x, y)
        isTurnX = not isTurnX
    else:
        print('Please try again!')


def checkWin():
    maps_flat = np.array(maps).flatten().tolist()
    if type_x not in maps_flat:
        print('O win!')
        return True
    if type_o not in maps_flat:
        print('X win!')
        return True
    # if type_none not in maps_flat:
    if 'q' in position:
        print('Wait to calculate...')
        point_x = maps_flat.count(type_x)
        point_o = maps_flat.count(type_o)
        print('\tPoint of X: ', point_x)
        print('\tPoint of Y: ', point_o)
        if point_x != point_o:
            win = 'X' if point_x > point_o else 'O'
            print('\t' + win + ' win!')
        else:
            print('\t~Equal~')
        return True
    return False


while True:
    printBoard()
    types = type_x if isTurnX else type_o
    position = input('Nhap toa do ' + types + ' (Enter "q" to end game): ')
    if checkWin():
        break
    pos_x, pos_y = [int(x) for x in position.split()]
    move(types, pos_x, pos_y)
