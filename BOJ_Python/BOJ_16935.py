# 배열 돌리기 3
def solve(num):
    tmp_N, tmp_M = len(A), len(A[0])
    if num == 1:
        tmp = [[0]*tmp_M for _ in range(tmp_N)]
        for i in range(tmp_N):
            for j in range(tmp_M):
                tmp[i][j] = A[tmp_N-i-1][j]
        return tmp
    elif num == 2:
        tmp = [[0]*tmp_M for _ in range(tmp_N)]
        for i in range(tmp_N):
            for j in range(tmp_M):
                tmp[i][j] = A[i][tmp_M-j-1]
        return tmp
    elif num == 3:
        tmp = [[0]*tmp_N for _ in range(tmp_M)]
        for i in range(tmp_M):
            for j in range(tmp_N):
                tmp[i][j] = A[tmp_N-j-1][i]
        return tmp
    elif num == 4:
        tmp = [[0]*tmp_N for _ in range(tmp_M)]
        for i in range(tmp_M):
            for j in range(tmp_N):
                tmp[i][j] = A[j][tmp_M-i-1]
        return tmp
    elif num == 5:
        tmp = [[0]*tmp_M for _ in range(tmp_N)]
        for i in range(tmp_N):
            for j in range(tmp_M):
                if i < tmp_N/2 and j < tmp_M/2:
                    tmp[i][j] = A[i+N//2][j]
                elif i < tmp_N/2 and j >= tmp_M/2:
                    tmp[i][j] = A[i][j-tmp_M//2]
                elif i >= tmp_N/2 and j >= tmp_M/2:
                    tmp[i][j] = A[i-tmp_N//2][j]
                elif i >= tmp_N/2 and j < tmp_M/2:
                    tmp[i][j] = A[i][j+tmp_M//2]
        return tmp
    elif num == 6:
        tmp = [[0]*tmp_M for _ in range(tmp_N)]
        for i in range(tmp_N):
            for j in range(tmp_M):
                if i < tmp_N/2 and j < tmp_M/2:
                    tmp[i][j] = A[i][j+tmp_M//2]
                elif i < tmp_N/2 and j >= tmp_M/2:
                    tmp[i][j] = A[i+tmp_N//2][j]
                elif i >= tmp_N/2 and j >= tmp_M/2:
                    tmp[i][j] = A[i][j-tmp_M//2]
                elif i >= tmp_N/2 and j < tmp_M/2:
                    tmp[i][j] = A[i-tmp_N//2][j]
        return tmp


N, M, R = map(int, input().split())
A = list(list(map(int, input().split())) for _ in range(N))
R_lst = map(int, input().split())
for i in R_lst:
    if i <= 0 or i > 6:
        continue
    A = solve(i)
for i in A:
    print(*i)