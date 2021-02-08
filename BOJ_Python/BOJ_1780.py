# 종이의 개수
N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
dfs()