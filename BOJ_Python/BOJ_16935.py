# 배열 돌리기 3
def solve(r):
    tmp = [[0]*m for _ in range(n)]
    if r == 1:
        for i in range(n):
            for j in range(m):
                tmp[i][j] = A[n-i-1][j]
        return tmp
    elif r == 2:
        for i in range(n):
            for j in range(m):
                tmp[i][j] = A[i][m-j-1]
        return tmp
    elif r == 3:
        for i in range(n):
            for j in range(m):
                tmp[i][j] = A[m-j-1][i]
        return tmp
    elif r == 4:
        for i in range(n):
            for j in range(m):
                tmp[i][j] = A[j][n-i-1]
        return tmp
    elif r == 5:
        for i in range(n):
            for j in range(m):
                if i < n/2 and j < m/2:
                    tmp[i][j] = A[i+n//2][j]
                elif i < n/2 and j >= m/2:
                    tmp[i][j] = A[i][j-m//2]
                elif i >= n/2 and j >= m/2:
                    tmp[i][j] = A[i-n//2][j]
                elif i >= n/2 and j < m/2:
                    tmp[i][j] = A[i][j+m//2]
        return tmp
    elif r == 6:
        for i in range(n):
            for j in range(m):
                if i < n/2 and j < m/2:
                    tmp[i][j] = A[i][j+m//2]
                elif i < n/2 and j >= m/2:
                    tmp[i][j] = A[i+n//2][j]
                elif i >= n/2 and j >= m/2:
                    tmp[i][j] = A[i][j-m//2]
                elif i >= n/2 and j < m/2:
                    tmp[i][j] = A[i-n//2][j]
        return tmp

n, m, R = map(int, input().split())
A = list(list(map(int, input().split())) for _ in range(n))
R_lst = map(int, input().split())
for i in R_lst:
    if i == 3 or i == 4:
        tmp = n
        n = m
        m = tmp
    A = solve(i)
for i in A:
    print(*i)