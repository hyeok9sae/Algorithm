# 다리 만들기
import sys
from collections import deque

def init(ny, nx):
    if 0 <= ny < N and 0 <= nx < N:
        return  True
    return False

def bfs_group(row, col, count):
    visited[row][col] = True
    matrix[row][col] = count
    deq = deque([(row, col)])
    while deq:
        y, x = deq.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not init(ny, nx):
                continue
            if matrix[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                matrix[ny][nx] = count
                deq.append((ny, nx))

def bfs(number):
    global ans
    dist = [[-1]*N for _ in range(N)]
    deq = deque([])
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == number:
                dist[i][j] = 0
                deq.append((i, j))
    while deq:
        y, x = deq.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not init(ny, nx):
                continue
            if matrix[ny][nx] != 0 and matrix[ny][nx] != number:
                ans = min(ans, dist[y][x])
                return
            if matrix[ny][nx] == 0 and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                deq.append((ny, nx))

N = int(input())
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
matrix = []
visited = [[False]*N for _ in range(N)]
count = 1
ans = sys.maxsize
for _ in range(N):
    matrix.append(list(map(int, input().split())))
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1 and not visited[i][j]:
            bfs_group(i, j, count)
            count += 1
for i in range(1, count):
        bfs(i)
print(ans)