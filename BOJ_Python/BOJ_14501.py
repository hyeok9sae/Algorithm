# 퇴사
def dfs(idx, res):
    if idx > N:
        global answer
        if answer < res:
            answer = res
        return
    dfs(idx+1, res)
    if idx+lst[idx][0] <= N+1:
        dfs(idx+lst[idx][0], res+lst[idx][1])

N = int(input())
lst = [(0, 0)]
for _ in range(N):
    T, P = map(int, input().split())
    lst.append((T, P))
answer = 0
dfs(1, 0)
print(answer)