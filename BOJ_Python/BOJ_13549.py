# 숨바꼭질 3
from collections import deque

def is_in(nv):
    if 0 <= nv <= 100000:
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
            flag = False
            if i == 0:
                flag = True
                nv = vertax * dx[i]
            else:
                nv = vertax + dx[i]
            if not is_in(nv):
                continue
            if visited[nv]:
                continue
            visited[nv] = True
            if not flag:
                deq.append((nv, cnt+1))
            else:
                deq.append((nv, cnt))

N, K = map(int, input().split())
dx = [2, -1, 1]
visited = [False]*100001
bfs(N)