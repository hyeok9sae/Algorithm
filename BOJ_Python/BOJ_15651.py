# N과 M (3)
def perm_repeat(lst, n, r):
    if r == 0:
        print(*tmp)
        return
    for i in range(n):
        tmp.append(i+1)
        perm_repeat(lst, n, r-1)
        tmp.pop()

N, M = map(int, input().split())
lst = [i+1 for i in range(N)]
tmp = []
perm_repeat(lst, N, M)