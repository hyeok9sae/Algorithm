# 알고스팟
from collections import deque

def is_in(ny, nx):
    if 0 <= ny < N and 0 <= nx < M:
        return True
    return False

def bfs(row, col):
    visited[row][col] = True
    deq = deque([(row, col, 0)])
    while deq:
        y, x, cnt = deq.popleft()
        if y == N-1 and x == M-1:
            print(cnt)
            return
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not is_in(ny, nx):
                continue
            if visited[ny][nx]:
                continue
            visited[ny][nx] = True
            if matrix[ny][nx] == '0':
                deq.appendleft((ny, nx, cnt))
            else:
                deq.append((ny, nx, cnt+1))

M, N = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(input()))
dy, dx = [0, -1, 0, 1], [-1, 0, 1, 0]
visited = [[False]*M for _ in range(N)]
bfs(0, 0)