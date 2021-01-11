# 트리의 지름
from collections import deque

def bfs(V):
    distance, vertax = 0, 0
    visited = [False for _ in range(N+1)]
    visited[V] = True
    deq = deque([(V, 0)])
    while deq:
        p, p_dist = deq.popleft()
        for i in dic[p]:
            if not visited[i[0]]:
                visited[i[0]] = True
                deq.append((i[0], p_dist + i[1]))
                if distance < p_dist + i[1]:
                    distance, vertax = p_dist + i[1], i[0]        
    return distance, vertax

N = int(input())
# matrix = [[] for _ in range(N+1)]
dic = {}
for _ in range(N):
    lst = list(map(int, input().split()))
    dic[lst[0]] = []
    for i in range(1, len(lst)-1, 2):
        dic[lst[0]].append((lst[i], lst[i+1]))
v1 = bfs(1)[1]
ans = bfs(v1)[0]
print(ans)