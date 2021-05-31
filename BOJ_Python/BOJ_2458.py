# 키 순서
N, M = map(int, input().split())
matrix = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = 1
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if matrix[i][k]+matrix[k][j] == 2:
                matrix[i][j] = 1
ans = 0
for k in range(1, N+1):
    cnt = 0
    for i in range(1, N+1):
        cnt += matrix[k][i] + matrix[i][k]
    if cnt == N-1:
        ans += 1
print(ans)