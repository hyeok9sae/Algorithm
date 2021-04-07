# N과 M (5)
def permutation(idx, n, r):
    if idx == r:
        print(*answer)
        return
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        answer.append(lst[i])
        permutation(idx+1, n, r)
        visited[i] = False
        answer.pop()

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
visited = [False]*N
answer = []
permutation(0, N, M)