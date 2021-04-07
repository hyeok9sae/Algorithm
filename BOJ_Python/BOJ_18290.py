# NM과 K (1)
N, M, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]
visited = [[False]*M for i in range(N)]
print(matrix)
print(visited)
print(N, M, K)