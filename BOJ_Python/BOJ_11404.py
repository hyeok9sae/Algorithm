# 플로이드
def floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    matrix[i][j] = 0
                    continue
                matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])

n = int(input())
m = int(input())
matrix = [[float('inf')]*(n) for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if matrix[a-1][b-1] < c:
        continue
    matrix[a-1][b-1] = c
# print(matrix)
floyd()
for i in matrix:
    for j in i:
        if j == float('inf'):
            print(0, end=" ")
        else:
            print(j, end=" ")
    print()