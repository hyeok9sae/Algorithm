# 그림
from collections import deque

def is_in(ny, nx):
    if 0 <= ny < n and 0 <= nx < m:
        return True
    return False

def bfs(row, col):
    visited[row][col] = True
    deq = deque([(row, col)])
    cnt = 1
    while deq:
        y, x = deq.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not is_in(ny, nx):
                continue
            if matrix[ny][nx] == 0 or visited[ny][nx]:
                continue
            visited[ny][nx] = True
            deq.append((ny, nx))
            cnt += 1
    return cnt

n, m = map(int, input().split())
matrix = list(list(map(int, input().split())) for _ in range(n))
visited = [[False]*m for _ in range(n)]
dy, dx = [0, -1, 0, 1], [-1, 0, 1, 0]
ans_size, ans_cnt = 0, 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1 and not visited[i][j]:
            ans_cnt += 1
            size = bfs(i, j)
            if ans_size < size:
                ans_size = size
print(ans_cnt, ans_size, sep="\n")