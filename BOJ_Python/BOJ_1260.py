# DFS와 BFS
from collections import deque

def dfs(V):
    visited[V] = True
    print(V, end=" ")
    for i in range(1, N+1):
        if matrix[V][i] == 1 and visited[i] == False:
            dfs(i)

def bfs(V):
    visited[V] = True
    deq = deque()
    deq.append(V)
    while deq:
        d = deq.popleft()
        print(d, end=" ")
        for i in range(1, N+1):
            if matrix[d][i] == 1 and visited[i] == False:
                visited[i] = True
                deq.append(i)

N, M, V = map(int, input().split())
matrix = list([0] * (N+1) for _ in range(N+1))
visited = list(False for _ in range(N+1))
for _ in range(M):
    y, x = map(int, input().split())
    matrix[y][x] = matrix[x][y] = 1

dfs(V)
print()
visited = list(False for _ in range(N+1))
bfs(V)