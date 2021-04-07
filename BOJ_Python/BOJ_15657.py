# N과 M (8)
def combination(idx, start, n, r):
    if idx == r:
        print(*answer)
        return
    for i in range(start, n):
        answer.append(lst[i])
        combination(idx+1, i, n, r)
        answer.pop()

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
answer = []
combination(0, 0, N, M)