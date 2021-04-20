# 숨바꼭질
from collections import deque

def is_in(nx):
    if 0 <= nx <= 100000:
        return True
    return False

def bfs(V):
    visited[V] = True
    deq = deque([(V, 0)])
    while deq:
        vertax, cnt = deq.popleft()
        if vertax == K:
            print(cnt)
            return
        for i in range(3):
            if i != 2:
                nx = vertax + dx[i]
            else:
                nx = vertax * dx[i]
            if not is_in(nx):
                continue
            if visited[nx]:
                continue
            visited[nx] = True
            deq.append((nx, cnt+1))

N, K = map(int, input().split())
dx = [-1, 1, 2]
visited = [False]*100001
bfs(N)