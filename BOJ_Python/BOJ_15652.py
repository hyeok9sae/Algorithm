# N과 M (4)
def comb_repeat(lst, start, n, r):
    if r == 0:
        print(*tmp)
        return
    for i in range(start, n):
        tmp.append(i+1)
        comb_repeat(lst, i, n, r-1)
        tmp.pop()

N, M = map(int, input().split())
lst = [i+1 for i in range(N)]
tmp = []
comb_repeat(lst, 0, N, M)