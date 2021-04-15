# 맞춰봐
def perm(r):
    if r == N:
        print(tmp)
        return
    if len(tmp) != 0:
        res = 0
        for i in range(len(tmp)):
            for j in range(len(tmp)):
                if i > j:
                    continue
                res += tmp[j]
                if matrix[i][j] == '-':
                    if res >= 0:
                        return
                elif matrix[i][j] == '0':
                    if res != 0:
                        return
                elif matrix[i][j] == '+':
                    if res <= 0:
                        return

    for idx, i in enumerate(num_lst):
        if visited[idx]:
            continue
        tmp.append(i)
        visited[idx] = True
        perm(r+1)
        tmp.pop()
        visited[idx] = False

N = int(input())
s = input()
matrix = [[""]*N for _ in range(N)]
pn = 0
for i in range(N):
    for j in range(N):
        if i > j:
            continue
        matrix[i][j] = s[pn]
        pn+=1
print(matrix)
num_lst = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
visited = [False]*len(num_lst)
tmp = []
for idx, i in enumerate(num_lst):
    tmp.append(i)
    visited[idx] = True
    perm(1)
    tmp.pop()
    visited[idx] = False
