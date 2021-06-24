# 줄 세우기
def dfs(v):
    if visited[v]:
        return
    visited[v] = True
    stack.append(v)
    for i in lst[v]:
        dfs(i)
    answer.append(stack[-1])
    stack.pop()

N, M = map(int, input().split())
lst = [[] for _ in range(N+1)]
# print(lst[0])
# lst[1].append(2)
# print(lst)
visited = [False]*(N+1)
stack = []
answer = []
for _ in range(M):
    A, B = map(int, input().split())
    lst[A].append(B)
# print(lst)
for i in range(1, N+1):
    dfs(i)
answer.reverse()
print(*answer)