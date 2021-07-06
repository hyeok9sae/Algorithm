# 미네랄 2
from collections import deque
def is_in(ny, nx):
    if 0 <= ny <= R and 0 <= nx <= C:
        return True
    return False

def check(row, col):
    if visited[row][col]:
        return
    visited[row][col] = True
    deq = deque()
    deq.append((row, col))
    while deq:
        y, x = deq.popleft()
        if y == R-1:
            return True
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not is_in(ny, nx):
                continue
            if matrix[ny][nx] == '.' or visited[ny][nx]:
                continue
            visited[ny][nx] = True
            deq.append((ny, nx))
    return False

def gravity():
    for i in range(R-2, -1, -1):
        for j in range(C):
            if matrix[i][j] == 'x' and visited[i][j]:
                matrix[i+1][j] = 'x'
                matrix[i][j] = '.'

def stick(order, row):
    if order%2 == 0:
        for i in range(C):
            if matrix[row][i] == 'x':
                matrix[row][i] = '.'
                return
    else:
        for i in range(C-1, -1, -1):
            if matrix[row][i] == 'x':
                matrix[row][i] = '.'
                return

R, C = map(int, input().split())
dy, dx = [0, -1, 0, 1], [-1, 0, 1, 0]
matrix = [list(input()) for _ in range(R)]
N = int(input())
height = list(map(int, input().split()))
for idx, h in enumerate(height):
    stick(idx, R-h)
    flag = False
    while not flag:
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 'x':
                    visited = [[False]*C for _ in range(R)]
                    if not check(i, j):
                        gravity()
                    else:
                        flag = True
                    
                    

for m in matrix:
    for n in m:
        print(n, end="")
    print()