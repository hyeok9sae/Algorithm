# 캐슬 디펜스
from itertools import combinations as cb
import copy

def check():
    for i in range(N):
        for j in range(M):
            if matr[i][j] == 1:
                return True
    return False

N, M, D = map(int, input().split())
matrix = list(list(map(int, input().split())) for _ in range(N))

array = [i for i in range(M)]
arr = list(cb(array, 3))
max = float('-inf')
for i in arr:
    cnt = 0
    lst = [0]*M
    for t in range(3):
        lst[i[t]] = 1
    matr = copy.deepcopy(matrix)
    matr.append(lst)
    while True:
        if not check():
            break

        ans = []
        for idx in range(M):
            if matr[N][idx] == 1:
                tmp = [float('inf'), float('inf'), float('inf')]
                for j in range(N):
                    for k in range(M):
                        if matr[j][k] == 1:
                            dist = abs(N-j)+abs(idx-k)
                            if dist <= D:
                                if tmp[0] < dist:
                                    continue
                                elif tmp[0] > dist:
                                    tmp = [dist, j, k]
                                else:
                                    if tmp[2] > k:
                                        tmp = [dist, j, k]
                if tmp[0] == float('inf') and tmp[1] == float('inf') and tmp[2] == float('inf'):
                    continue
                ans.append((tmp[1], tmp[2]))
        for a, b in ans:
            # print(ans)
            if matr[a][b] == 1:
                matr[a][b] = 0
                cnt += 1
        for c in range(N-1, 0, -1):
            matr[c] = matr[c-1]
        matr[0] = [0]*M
        # print(matr, 1)

    # print(matr)
    if max < cnt:
        max = cnt
    matr.pop()
print(max)