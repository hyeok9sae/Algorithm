# 나이트의 이동
from collections import deque

def is_in(i, j):
    if 0 <= i < l and 0 <= j < l:
        return True
    return False

def bfs():
    visited[n][m] = True
    deq = deque([(n, m, 0)])
    while deq:
        y, x, cnt = deq.popleft()
        if y == N and x == M:
                global ans
                ans = cnt
                return
        for i in range(8):
            ny, nx = y + dy[i], x + dx[i]
            if not is_in(ny, nx):
                continue
            if visited[ny][nx]:
                continue
            visited[ny][nx] = True
            deq.append((ny, nx, cnt+1))

dy = [-1, -2, -2, -1, 1, 2, 2, 1]
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
T = int(input())
for _ in range(T):
    l = int(input())
    n, m = map(int, input().split())
    N, M = map(int, input().split())
    ans = 0
    visited = [[False]*l for _ in range(l)]
    bfs()
    print(ans)