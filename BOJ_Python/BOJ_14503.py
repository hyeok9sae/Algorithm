# 로봇 청소기
def sweep(row, col):
    global d
    flag = False
    visited[row][col] = True
    for i in range(4):
        ny, nx = row+dy[(3-d)%4], col+dx[(3-d)%4]
        d = (3-d)%4
        if matrix[ny][nx] != 1 and not visited[ny][nx]:
            sweep(ny, nx)
            flag = True
            break
    if not flag:
        ny, nx = row+dy[(d-2)%4], col+dx[(d-2)%4]
        if matrix[ny][nx] != 1:
            sweep(ny, nx)
        else:
            return
    

N, M = map(int, input().split())
r, c, d = map(int, input().split())
visited = [[False]*M for _ in range(N)]
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
matrix = [[*map(int, input().split())] for _ in range(N)]
sweep(r, c)
ans = 0
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            ans += 1
print(ans)