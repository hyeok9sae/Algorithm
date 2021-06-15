# 미세먼지 안녕!
def is_in(ny, nx):
    if 0 <= ny < R and 0 <= nx < C:
        return True
    return False

def diffusion(row, col):
    count = 0
    for i in range(4):
        ny, nx = row + dy[i], col + dx[i]
        if not is_in(ny, nx) or matrix[ny][nx] == -1:
            continue
        count += 1
        if (ny, nx) not in dic:
            dic[(ny, nx)] = []
        dic[(ny, nx)].append(matrix[row][col] // 5)
    dic[(row, col)].append(matrix[row][col]-(matrix[row][col] // 5)*count)
def check(row, col):
    if (row, col) not in dic:
        dic[(row, col)] = []
    diffusion(row, col)

def purification(row, col, flag):
    if not flag:
        temp = matrix[0][0]
        for i in range(C-1):
            if matrix[0][i+1] == -1:
                matrix[0][i] = 0
                continue
            if matrix[0][i] == -1:
                continue
            matrix[0][i] = matrix[0][i+1]
        for i in range(row):
            if matrix[i+1][C-1] == -1:
                matrix[i][C-1] = 0
                continue
            if matrix[i][C-1] == -1:
                continue
            matrix[i][C-1] = matrix[i+1][C-1]
        for i in range(C-1, 0, -1):
            if matrix[row][i-1] == -1:
                matrix[row][i] = 0
                continue
            if matrix[row][i] == -1:
                continue
            matrix[row][i] = matrix[row][i-1]
        for i in range(row, 1, -1):
            if matrix[i-1][0] == -1:
                matrix[i][0] = 0
                continue
            if matrix[i][0] == -1:
                continue
            matrix[i][0] = matrix[i-1][0]
        if temp == -1:
            matrix[1][0] = 0
        else:
            matrix[1][0] = temp
    else:
        temp = matrix[row][0]
        for i in range(row, R-1):
            if matrix[i+1][0] == -1:
                matrix[i][0] = 0
                continue
            if matrix[i][0] == -1:
                continue
            matrix[i][0] = matrix[i+1][0]
        for i in range(C-1):
            if matrix[R-1][i+1] == -1:
                matrix[R-1][i] = 0
                continue
            if matrix[R-1][i] == -1:
                continue
            matrix[R-1][i] = matrix[R-1][i+1]
        for i in range(R-1, row-1, -1):
            if matrix[i-1][C-1] == -1:
                matrix[i][C-1] = 0
                continue
            if matrix[i][C-1] == -1:
                continue
            matrix[i][C-1] = matrix[i-1][C-1]
        for i in range(C-1, 1, -1):
            if matrix[row][i-1] == -1:
                matrix[row][i] = 0
                continue
            if matrix[row][i] == -1:
                continue
            matrix[row][i] = matrix[row][i-1]
        if temp == -1:
            matrix[row][1] = 0
        else:
            matrix[row][1] = temp

R, C, T = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(R)]
dy, dx = [0, -1, 0, 1], [-1, 0, 1, 0]
for _ in range(T):
    dic = {}
    for i in range(R):
        for j in range(C):
            if matrix[i][j] != -1 and matrix[i][j] != 0:
                check(i, j)
    for i, j in dic:
        matrix[i][j] = sum(dic[(i, j)])
    flag = False
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == -1:
                purification(i, j, flag)
                flag = True
answer = 0
for i in range(R):
    for j in range(C):
        if matrix[i][j] == -1:
            continue
        answer += matrix[i][j]
print(answer)