# 모든 순열
# def swap(i, j):
#     tmp = lst[i]
#     lst[i] = lst[j]
#     lst[j] = tmp
    
def permutation(r):
    if r == N:
        print(*tmp)
        return
    for i in range(N):
        if not visited[i]:
            # swap(i, r)
            visited[i] = True
            tmp.append(i+1)
            permutation(r+1)
            # swap(i, r)
            visited[i] = False
            tmp.pop()

N = int(input())
lst = [i+1 for i in range(N)]
tmp = []
visited = [False]*N
permutation(0)