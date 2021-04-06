# N과 M (2)
def combination(lst, visited, start, n, r):
    if r == 0:
        for i in range(n):
            if visited[i]:
                print(lst[i], end=" ")
        print("")
        return

    for i in range(start, n):
        visited[i] = True
        combination(lst, visited, i+1, n, r-1)
        visited[i] = False

N, M = map(int, input().split())
lst = [i+1 for i in range(N)]
visited = [False for i in range(N)]
combination(lst, visited, 0, N, M)