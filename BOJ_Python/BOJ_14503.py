# 로봇 청소기
def is_in(ny, nx):
    if 0 <= ny < N and 0 <= nx < M:
        return True
    return False

def solve(row, col):
    global d
    if not sweep[row][col]:
        global ans
        ans += 1
        sweep[row][col] = True
    flag = False
    for i in range(4):
        d = (d-1)%4
        ny, nx = row + dy[d], col + dx[d]
        if not is_in(ny, nx):
            if i == 3:
                flag = True
            continue
        if matrix[ny][nx] == 1 or sweep[ny][nx]:
            if i == 3:
                flag = True
            continue
        solve(ny, nx)
        break
    if flag:
        ny, nx = row + dy[d-2], col + dx[d-2]
        if matrix[ny][nx] != 1:
            solve(ny, nx)
        else:
            return

N, M = map(int, input().split())
r, c, d = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(N)]
sweep = [[False]*M for _ in range(N)]
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
ans = 0
solve(r, c)
print(ans)