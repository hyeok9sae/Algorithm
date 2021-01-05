# 연결 요소의 개수
def dfs(V):
    visited[V] = True
    for i in range(1, N+1):
        if matrix[V][i] == 1 and visited[i] == False:
            dfs(i)

N, M = map(int, input().split())
matrix = [[0] * (N+1) for _ in range(N+1)]
visited = [False for _ in range(N+1)]
cnt = 0
for _ in range(M):
    u, v = map(int, input().split())
    matrix[u][v] = matrix[v][u] = 1
for i in range(1, N+1):
    if visited[i] == False:
        dfs(i)
        cnt += 1
print(cnt)

