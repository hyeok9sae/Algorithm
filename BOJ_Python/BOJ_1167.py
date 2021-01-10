# 트리의 지름
from collections import deque

def bfs(V):
    distance = 0
    visited[V] = True
    deq = deque([])
    deq.append((V, 0))
    while deq:
        p, p_dist = deq.popleft()
        for i in range(len(matrix[p])):
            if not visited[matrix[p][i]]:
                visited[matrix[p][i]] = True
                deq.append((matrix[p][i], p_dist + dist[p][matrix[p][i]]))
                if p_dist + dist[p][matrix[p][i]] > distance:
                    distance = p_dist + dist[p][matrix[p][i]]             
    return distance

N = int(input())
matrix = [[] for _ in range(N+1)]
dist = [[0]*(N+1) for _ in range(N+1)]
ans = []
for _ in range(N):
    lst = list(map(int, input().split()))
    for i in range(1, len(lst)-1, 2):
        matrix[lst[0]].append(lst[i])
        matrix[lst[i]].append(lst[0])
        dist[lst[0]][lst[i]] = dist[lst[i]][lst[0]] = lst[i+1]
for i in range(1, N+1):
    visited = [False for _ in range(N+1)]
    ans.append(bfs(i))
print(max(ans))   