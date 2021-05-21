# 주사위 굴리기
def is_in(ny, nx):
    if 0 <= ny < N and 0 <= nx < M:
        return True
    return False

def move(n):
    global y, x
    ny, nx = y + dy[n], x + dx[n]
    # print(ny, nx)
    if not is_in(ny, nx):
        return False
    y, x = ny, nx
    if n == 1:
        tmp = dice[1][2]
        dice[1][2] = dice[1][1]
        dice[1][1] = dice[1][0]
        dice[1][0] = dice[3][1]
        dice[3][1] = tmp
    elif n == 2:
        tmp = dice[1][0]
        dice[1][0] = dice[1][1]
        dice[1][1] = dice[1][2]
        dice[1][2] = dice[3][1]
        dice[3][1] = tmp
    elif n == 3:
        tmp = dice[0][1]
        dice[0][1] = dice[1][1]
        dice[1][1] = dice[2][1]
        dice[2][1] = dice[3][1]
        dice[3][1] = tmp
    else:
        tmp = dice[3][1]
        dice[3][1] = dice[2][1]
        dice[2][1] = dice[1][1]
        dice[1][1] = dice[0][1]
        dice[0][1] = tmp
    if matrix[y][x] == 0:
        matrix[y][x] = dice[3][1]
    else:
        dice[3][1] = matrix[y][x]
        matrix[y][x] = 0
    return True
N, M, y, x, K = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(N)]
command = [*map(int, input().split())]
dice = [[-1, 0, -1], [0, 0, 0], [-1, 0, -1], [-1, 0, -1]]
dy, dx = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]
for cmd in command:
    if move(cmd):
        # print(y, x)
        # print(dice[3][1])
        print(dice[1][1])
        # print(*dice, sep="\n")