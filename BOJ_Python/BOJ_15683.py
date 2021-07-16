# 감시
def watch(row, col, dir):
    ny, nx = row, col
    visited[ny][nx] -= 1
    while True:
        ny, nx = ny+dy[dir], nx+dx[dir]
        if not is_in(ny, nx):
            break
        if matrix[ny][nx] == 6:
            break
        if matrix[ny][nx] != 0:
            continue
        visited[ny][nx] -= 1

def de_watch(row, col, dir):
    ny, nx = row, col
    visited[ny][nx] += 1
    while True:
        ny, nx = ny+dy[dir], nx+dx[dir]
        if not is_in(ny, nx):
            break
        if matrix[ny][nx] == 6:
            break
        if matrix[ny][nx] != 0:
            continue
        visited[ny][nx] += 1

def is_in(ny, nx):
    if 0 <= ny < N and 0 <= nx < M:
        return True
    return False

def cal():
    count = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] >= 0 and matrix[i][j] == 0:
                count += 1
    return count

def check(cnt):
    if cnt == countd:
        answer = cal()
        global max_answer
        if max_answer > answer:
            max_answer = answer
        return
    num, n, m = cctv[cnt]
    if num == 1:
        for i in range(4):
            watch(n, m, i)
            check(cnt+1)
            de_watch(n, m, i)
    elif num == 2:
        for i in range(2):
            watch(n, m, i)
            watch(n, m, i+2)
            check(cnt+1)
            de_watch(n, m, i)
            de_watch(n, m, i+2)
    elif num == 3:
        for i in range(4):
            watch(n, m, i)
            watch(n, m, (i+1)%4)
            check(cnt+1)
            de_watch(n, m, i)
            de_watch(n, m, (i+1)%4)
    elif num == 4:
        for i in range(4):
            watch(n, m, i)
            watch(n, m, (i+1)%4)
            watch(n, m, (i+2)%4)
            check(cnt+1)
            de_watch(n, m, i)
            de_watch(n, m, (i+1)%4)
            de_watch(n, m, (i+2)%4)
    elif num == 5:
        for i in range(4):
            watch(n, m, i)
        check(cnt+1)
        for i in range(4):
            de_watch(n, m, i)

N, M = map(int, input().split())
matrix = list(list(map(int, input().split())) for _ in range(N))
dy, dx = (0, -1, 0, 1), (-1, 0, 1, 0)
visited = [[0]*M for _ in range(N)]
countd = 0
cctv = []
for i in range(N):
    for j in range(M):
        if 1 <= matrix[i][j] <= 5:
            countd += 1
            cctv.append([matrix[i][j], i, j])
max_answer = float('inf')
check(0)

print(max_answer)