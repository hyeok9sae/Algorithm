# 숨바꼭질 4
from collections import deque

def is_in(nV):
    if 0 <= nV <= 100000:
        return True
    return False

def bfs(V):
    visited[V] = True
    deq = deque([(V, 0)])
    while deq:
        vertax, cnt = deq.popleft()
        if vertax == K:
            print(cnt)
            ans.append(vertax)
            while prev[vertax] != -1:
                ans.appendleft(prev[vertax])
                vertax = prev[vertax]
            print(*ans)
            return
        for i in range(3):
            if i != 2:
                nV = vertax + dx[i]
            else:
                nV = vertax * dx[i]
            if not is_in(nV):
                continue
            if visited[nV]:
                continue
            visited[nV] = True
            prev[nV] = vertax
            deq.append((nV, cnt+1))

N, K = map(int, input().split())
dx = [-1, 1, 2]
visited = [False]*100001
prev = [-1]*100001
ans = deque()
bfs(N)