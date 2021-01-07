# 단지번호붙이기
from collections import deque

def bfs(row, col):
    cnt = 0
    visited[row][col] = True
    deq = deque([(row, col)])
    while deq:
        y, x = deq.popleft()
        cnt += 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                continue
            if matrix[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                deq.append([ny, nx])
    return cnt

N = int(input())
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
matrix = []
ans = []
visited = [[False]*N for _ in range(N)]
for i in range(N):
    matrix.append(list(map(int, input())))
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1 and not visited[i][j]:
            ans.append(bfs(i, j))
ans.sort()
print(len(ans))
print(*ans, sep="\n")