# 외판원 순회 2
def perm(r):
    if len(lst) > 1:
        if matrix[lst[-2]][lst[-1]] == 0:
            return

    if r == N:
        global min
        res = 0
        for i in range(N-1):
            res += matrix[lst[i]][lst[i+1]]
        
        if matrix[lst[-1]][lst[0]] == 0:
            return
        res += matrix[lst[-1]][lst[0]]
        if min > res:
            min = res
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            lst.append(i)
            perm(r+1)
            visited[i] = False
            lst.pop()

N = int(input())
matrix = [list(map(int, input().split())) for i in range(N)]
lst = []
min = float('inf')
visited = [False]*N
perm(0)
print(min)