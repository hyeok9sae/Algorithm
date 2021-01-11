# 트리의 지름
from collections import deque

def bfs(V):
    vert, dist = 0, 0
    visited = [False for _ in range(N+1)]
    visited[V] = True
    deq = deque([(V, 0)])
    while deq:
        p_vert, p_dist = deq.popleft()
        for i in dic[p_vert]:
            if not visited[i[0]]:
                visited[i[0]] = True
                deq.append((i[0], p_dist + i[1]))
                # print(p_vert, p_dist)
                if dist < p_dist + i[1]:
                    dist = p_dist + i[1]
                    vert = i[0]
    return vert, dist

N = int(input())
dic = {}
for i in range(N+1):
    dic[i] = []
for _ in range(N-1):
    P, C, W = map(int, input().split()) #부모, 자식, 가중치
    dic[P].append((C, W))
    dic[C].append((P, W))
v1 = bfs(1)[0]
# print(v1)
print(bfs(v1)[1])