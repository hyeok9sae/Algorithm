# 섬의 개수
from collections import deque

def bfs(row, col):
    visited[row][col] = True
    deq = deque([(row, col)])
    while deq:
        y, x = deq.popleft()
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= h or nx >= w:
                continue
            if matrix[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                deq.append((ny, nx))

dy = [0, 0, -1, 1, -1, -1, 1, 1]
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    matrix = []
    visited = [[False]*w for _ in range(h)]
    cnt = 0
    for _ in range(h):
        matrix.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    print(cnt)
