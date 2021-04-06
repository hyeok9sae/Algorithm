# N과 M (1)
def permutation(lst, visited, n, r):
    if r == 0:
        print(*tmp)
        return
    for i in range(n): 
        if not visited[i]:
            visited[i] = True
            tmp.append(i+1)
            permutation(lst, visited, n, r-1)
            visited[i] = False
            tmp.pop()

N, M = map(int, input().split())
visited = [False]*N
tmp = []
lst = [i for i in range(1, N+1)]
permutation(lst, visited, N, M)