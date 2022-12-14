from sys import stdout

n = int(input())
x, y = map(int,input().split())

UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT = 0, 1, 2, 3
grid = [['+'] * n for _ in range(n)]
grid[x - 1][y - 1] = '.'

def resolve(i, j, i_manq, j_manq, letter, size):
    if size == 2:
        for di, dj in ((0, 0), (0, 1), (1, 1), (1, 0)):
            if grid[i + di][j + dj] == '+':
                grid[i + di][j + dj] = letter
    else:
        if size == 4:
            A = 'A'; B = 'B'; C = 'C'; D = 'D'
        else:
            A = B = C = D = letter

        if i <= i_manq < i + size // 2:
            ZONE = UP_LEFT if j <= j_manq < j + size // 2 else UP_RIGHT
        else:
            ZONE = DOWN_LEFT if j <= j_manq < j + size // 2 else DOWN_RIGHT

        if ZONE != UP_LEFT:
            grid[i + size // 2 - 1][j + size // 2 - 1] = letter
        if ZONE != UP_RIGHT:
            grid[i + size // 2 - 1][j + size // 2] = letter
        if ZONE != DOWN_LEFT:
            grid[i + size // 2][j + size // 2 - 1] = letter
        if ZONE != DOWN_RIGHT:
            grid[i + size // 2][j + size // 2] = letter

        if ZONE != UP_LEFT:
            resolve(i, j, i + size // 2 - 1, j + size // 2 - 1, A, size // 2)
        else:
            resolve(i, j, i_manq, j_manq, A, size // 2)

        if ZONE != UP_RIGHT:
            resolve(i, j + size // 2, i + size // 2 - 1, j + size // 2, B, size // 2)
        else:
            resolve(i, j + size // 2, i_manq, j_manq, B, size // 2)

        if ZONE != DOWN_LEFT:
            resolve(i + size // 2, j, i + size // 2, j + size // 2 - 1, C, size // 2)
        else:
            resolve(i + size // 2, j, i_manq, j_manq, C, size // 2)

        if ZONE != DOWN_RIGHT:
            resolve(i + size // 2, j + size // 2, i + size // 2, j + size // 2, D, size // 2)
        else:
            resolve(i + size // 2, j + size // 2, i_manq, j_manq, D, size // 2)

if n == 1:
    print('.')

else:
    resolve(0, 0, x - 1, y - 1, 'Z', n)

    for k in range(n):
        stdout.write(''.join(grid[k]) + '\n') 
