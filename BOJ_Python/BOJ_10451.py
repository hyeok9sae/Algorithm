# 순열 사이클
def dfs(V):
    visited[V] = True
    if not visited[lst[V-1]]:
        dfs(lst[V-1])
    return True

T = int(input())
for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    visited = [False for _ in range(len(lst)+1)]
    cnt = 0
    for i in range(len(lst)):
        if not visited[lst[i]]:
            if dfs(lst[i]):
                cnt += 1
    print(cnt)