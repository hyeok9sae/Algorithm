# 미로 탐색
from collections import deque

def init(row, col):
    if row < 0 or col < 0 or row >= N or col >= M:
        return False
    return True

def bfs(row, col):
    visited[row][col] = True
    deq = deque([(row, col)])
    while deq:
        y, x = deq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not init(ny, nx):
                continue
            if matrix[ny][nx] == 1 and not visited[ny][nx]:
                matrix[ny][nx] = matrix[y][x] + 1
                visited[ny][nx] = True
                deq.append((ny, nx))

N, M = map(int, input().split())
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
matrix = []
visited = [[False]*M for _ in range(N)]
for _ in range(N):
    matrix.append(list(map(int, input())))
bfs(0, 0)
# print(matrix)
print(matrix[N-1][M-1])