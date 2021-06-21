# 우수 마을
import sys
sys.setrecursionlimit(100000)

def dfs(cur):
    visited[cur] = True
    dp[cur][0] = lst[cur]
    for i in matrix[cur]:
        if not visited[i]:
            dfs(i)
            dp[cur][0] += dp[i][1]
            dp[cur][1] += max(dp[i][1], dp[i][0])

N = int(input())
lst = [0] + list(map(int, input().split()))
matrix = [[] for _ in range(N+1)]
visited = [False]*(N+1)
dp = [[0]*2 for _ in range(N+1)]
for _ in range(N-1):
    v, u = map(int, input().split())
    matrix[v].append(u)
    matrix[u].append(v)
dfs(1)
print(max(dp[1][1], dp[1][0]))