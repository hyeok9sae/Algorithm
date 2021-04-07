# N과 M (7)
def permutation(idx, n, r):
    if idx == r:
        print(*answer)
        return
    for i in range(n):
        answer.append(lst[i])
        permutation(idx+1, n, r)
        answer.pop()

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
answer = []
permutation(0, N, M)