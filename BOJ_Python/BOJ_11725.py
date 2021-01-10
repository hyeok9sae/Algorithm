# 트리의 부모 찾기
from collections import deque

def bfs(V):
    visited[V] = True
    deq = deque([])
    deq.append(V)
    while deq:
        parent = deq.popleft()
        for i in range(len(matrix[parent])):
            if not visited[matrix[parent][i]]:
                visited[matrix[parent][i]] = True
                deq.append(matrix[parent][i])
                ans[matrix[parent][i]] = parent

N = int(input())
matrix = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
ans = [0 for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)
for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
print(*ans[2:])