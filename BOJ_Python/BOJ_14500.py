# 테트로미노
N, M = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(N)]
ans = float('-inf')
for i in range(N):
    for j in range(M):
        if j+3 < M:
            res = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i][j+3]
            if ans < res:
                ans = res
        if i+3 < N:
            res = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+3][j]
            if ans < res:
                ans = res
        if j+1 < M and i+1 < N:
            res = matrix[i][j] + matrix[i][j+1] + matrix[i+1][j] + matrix[i+1][j+1]
            if ans < res:
                ans = res
        if j+1 < M and i+2 < N:
            res = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+2][j+1]
            if ans < res:
                ans = res
        if j+2 < M and i+1 < N:
            res = matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+1][j+2] + matrix[i][j+2]
            if ans < res:
                ans = res
        if j+1 < M and i+2 < N:
            res = matrix[i][j] + matrix[i][j+1] + matrix[i+1][j+1] + matrix[i+2][j+1]
            if ans < res:
                ans = res
        if j+2 < M and i+1 < N:
            res = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j]
            if ans < res:
                ans = res
        if j+1 < M and i+2 < N:
            res = matrix[i][j] + matrix[i][j+1] + matrix[i+1][j] + matrix[i+2][j]
            if ans < res:
                ans = res
        if j+2 < M and i+1 < N:
            res = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j+2]
            if ans < res:
                ans = res
        if j+1 < M and i+2 < N:
            res = matrix[i][j+1] + matrix[i+1][j+1] + matrix[i+2][j+1] + matrix[i+2][j]
            if ans < res:
                ans = res
        if j+2 < M and i+1 < N:
            res = matrix[i][j] + matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+1][j+2]
            if ans < res:
                ans = res
        # 초록
        if j+1 < M and i+2 < N:
            res = matrix[i][j] + matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+2][j+1]
            if ans < res:
                ans = res
        if j+1 < M and i+2 < N:
            res = matrix[i][j+1] + matrix[i+1][j+1] + matrix[i+1][j] + matrix[i+2][j]
            if ans < res:
                ans = res
        if j+2 < M and i+1 < N:
            res = matrix[i][j] + matrix[i][j+1] + matrix[i+1][j+1] + matrix[i+1][j+2]
            if ans < res:
                ans = res
        if j+2 < M and i+1 < N:
            res = matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j] + matrix[i+1][j+1]
            if ans < res:
                ans = res
        # 핑크
        if j+2 < M and i+1 < N:
            res = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j+1]
            if ans < res:
                ans = res
        if j+1 < M and i+2 < N:
            res = matrix[i][j+1] + matrix[i+1][j+1] + matrix[i+1][j] + matrix[i+2][j+1]
            if ans < res:
                ans = res
        if j+1 < M and i+2 < N:
            res = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+1][j+1]
            if ans < res:
                ans = res
        if j+2 < M and i+1 < N:
            res = matrix[i][j+1] + matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+1][j+2]
            if ans < res:
                ans = res 
print(ans)