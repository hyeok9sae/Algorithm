# 아기 상어
from collections import deque

def is_in(ny, nx):
    if 0 <= ny < N and 0 <= nx < N:
        return True
    return False

def check_fish(row, col, size):
    fish_cnt = 0
    for i in range(N):
        for j in range(N):
            if i == row and j == col:
                continue
            if 0 < matrix[i][j] < size:
                fish_cnt += 1
    return fish_cnt

def start(row, col):
    shark_size = 2
    cnt = 0
    matrix[row][col] = 0
    while True:
        if check_fish(row, col, shark_size) == 0:
            break
        else:
            row, col, time = bfs(row, col, shark_size)
            if time == -1:
                break
            global ans
            ans += time
            cnt += 1
            if cnt == shark_size:
                shark_size += 1
                cnt = 0
            matrix[row][col] = 0
    return

def bfs(row, col, shark_size):
    visited = [[False]*N for _ in range(N)]
    deq = deque([])
    deq.append((row, col, 0))
    fish = []
    while deq:
        y, x, time = deq.popleft()
        if 0 < matrix[y][x] < shark_size:
            fish.append((y, x, time))
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not is_in(ny, nx):
                continue
            if matrix[ny][nx] > shark_size or visited[ny][nx]:
                continue
            visited[ny][nx] = True
            deq.append((ny, nx, time+1))
    fish.sort(key=lambda x:x[1])
    fish.sort(key=lambda x:x[0])
    fish.sort(key=lambda x:x[2])
    if len(fish) == 0:
        return -1, -1, -1
    return fish[0]

N = int(input())
dy, dx = [0, -1, 0, 1], [-1, 0, 1, 0]
matrix = [[*map(int, input().split())] for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 9:
            start(i, j)
print(ans)

# 아기 상어의 처음 위치(9)를 못지나가는 문제가 발생
# 아기 상어(9)를 물고기로 인식하는 문제가 발생
# deque에 초기화 하면서 바로 값을 넣는 것과 초기화 후 값을 넣는 것의 차이