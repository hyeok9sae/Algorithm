# ABCDE
def dfs(V, cnt):
    global is_finish
    if is_finish:
        return
    if cnt == 4:
        is_finish = True
        return
    for i in lst[V]:
        if not visited[i]:
            visited[i] = True
            dfs(i, cnt+1)
            visited[i] = False

N, M = map(int, input().split())
is_finish = False
lst = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
# print(lst)
# print(dic)
for i in range(N):
    if is_finish:
        break
    visited = [False]*N
    visited[i] = True
    dfs(i, 0)
if is_finish:
    print(1)
else:
    print(0)