# 토마토
from collections import deque

def bfs():
    while deq:
        y, x = deq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= M:
                continue
            if matrix[ny][nx] == 0:
                matrix[ny][nx] = matrix[y][x] + 1
                deq.append((ny, nx))

deq = deque()
M, N = map(int, input().split())
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
matrix = []
isRipe = False
for _ in range(N):
    matrix.append(list(map(int, input().split())))
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            deq.append((i, j))
bfs()
for i in matrix:
    if isRipe:
        break
    for j in i:
        if j == 0:    
            print(-1)
            isRipe = True
            break
if not isRipe:
    print(max(map(max, matrix))-1)