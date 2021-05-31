# 배열 돌리기 6
def check(k, l):
    for i in range(0, 2**N, 2**l):
        for j in range(0, 2**N, 2**l):
            rotate(i, j, 2**l, k)
    if 5 <= k <= 8:
        for i in range(2**N):
            for j in range(2**N):
                matrix[i][j] = lst[i][j]

def rotate(row, col, size, k):
    tmp, gn = [], 0
    for i in range(row, row+size):
        for j in range(col, col+size):
            tmp.append(matrix[i][j])
    if k == 1:
        for i in range(row+size-1, row-1, -1):
            for j in range(col, col+size):
                matrix[i][j] = tmp[gn]
                gn += 1
    elif k == 2:
        for i in range(row, row+size):
            for j in range(col+size-1, col-1, -1):
                matrix[i][j] = tmp[gn]
                gn += 1
    elif k == 3:
        for i in range(col+size-1, col-1, -1):
            for j in range(row, row+size):
                matrix[j][i] = tmp[gn]
                gn += 1
    elif k == 4:
        for i in range(col, col+size):
            for j in range(row+size-1, row-1, -1):
                matrix[j][i] = tmp[gn]
                gn += 1
    elif k == 5:
        for i in range(2**N-(row+size), 2**N-(row+size)+size):
            for j in range(col, col+size):
                lst[i][j] = tmp[gn]
                gn += 1
    elif k == 6:
        for i in range(row, row+size):
            for j in range(2**N-(col+size), 2**N-(col+size)+size):
                lst[i][j] = tmp[gn]
                gn += 1
    elif k == 7:
        for i in range(col, col+size):
            for j in range(2**N-(row+size), 2**N-(row+size)+size):
                lst[i][j] = tmp[gn]
                gn += 1
    elif k == 8:
        for i in range(2**N-(col+size), 2**N-(col+size)+size):
            for j in range(row, row+size):
                lst[i][j] = tmp[gn]
                gn += 1
                
N, R = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(2**N)]
lst = [[0]*(2**N) for _ in range(2**N)]
for i in range(R):
    k, l = map(int, input().split())
    check(k, l)
for i in matrix:
    print(*i)