# 로또
def comb(start, r):
    if r == 6:
        print(*ans)
        return
    for i in range(start, k):
        ans.append(S[i])
        comb(i+1, r+1)
        ans.pop()
while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        break
    k, S = lst[0], lst[1:]
    ans = []
    comb(0, 0)
    print()