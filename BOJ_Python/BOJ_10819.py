# 차이를 최대로
def perm(r):
    if r == N:
        global max
        res = 0
        for i in range(N-1):
            res += abs(tmp[i]-tmp[i+1])
        # print(tmp, res)
        if max < res:
            max = res
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            tmp.append(lst[i])
            perm(r+1)
            visited[i] = False
            tmp.pop()

N = int(input())
lst = list(map(int, input().split()))
# lst.sort()
visited = [False]*N
tmp = []
max = float('-inf')
perm(0)
print(max)