# 상어 중학교
from collections import deque

def is_in(ny, nx):
    if 0 <= ny < N and 0 <= nx < N:
        return True
    return False

def bfs(row, col):
    number = matrix[row][col]
    visited[row][col] = True
    deq = deque([(row, col, 0)])
    rainbow = 0
    lst = []
    while deq:
        y, x, cnt = deq.popleft()
        lst.append((y, x))
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not is_in(ny, nx):
                continue
            if matrix[ny][nx] != number and matrix[ny][nx] != 0:
                continue
            if visited[ny][nx]:
                continue
            if matrix[ny][nx] == 0:
                rainbow += 1
            visited[ny][nx] = True
            deq.append((ny, nx, cnt+1))
    return rainbow, len(lst), lst, row, col

N, M = map(int, input().split())
matrix = list(list(map(int, input().split())) for _ in range(N))
dy, dx = [0, -1, 0, 1], [-1, 0, 1, 0]
ans = 0
for _ in range(M):
    
    max_size, max_rain, max_tmp, std_row, std_col = 0, 0, [], 0, 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] <= -1:
                continue
            if matrix[i][j] == 0:
                continue
            visited = [[False]*N for _ in range(N)]
            rain_cnt, size, tmp, row, col = bfs(i, j)
            # print(rain_cnt, size, tmp, row, col)
            if max_size < size:
                max_size = size
                max_rain = rain_cnt
                max_tmp = tmp
                std_row = row
                std_col = col
            elif max_size == size:
                if max_rain < rain_cnt:
                    max_size = size
                    max_rain = rain_cnt
                    max_tmp = tmp
                    std_row = row
                    std_col = col
                elif max_rain == rain_cnt:
                    if std_row < row:
                        max_size = size
                        max_rain = rain_cnt
                        max_tmp = tmp
                        std_row = row
                        std_col = col
                    elif std_row == row:
                        if std_col < col:
                            max_size = size
                            max_rain = rain_cnt
                            max_tmp = tmp
                            std_row = row
                            std_col = col
    score = 0
    print(max_tmp)
    for i, j in max_tmp:
        matrix[i][j] = -2
        score += 1
    ans += score*score
    print(ans)
    for i in range(N-2, -1, -1):
        for j in range(N):
            if matrix[i][j] <= -1:
                continue
            t = i
            while True:
                if t == N-1:
                    break
                cur = matrix[t][j]
                next = matrix[t+1][j]
                if next != -2:
                    break
                matrix[t][j] = next
                matrix[t+1][j] = cur
                t += 1
    tmp = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp[i][j] = matrix[j][N-i-1]
    matrix = tmp
    for i in range(N-2, -1, -1):
        for j in range(N):
            if matrix[i][j] <= -1:
                continue
            t = i
            while True:
                if t == N-1:
                    break
                cur = matrix[t][j]
                next = matrix[t+1][j]
                if next != -2:
                    break
                matrix[t][j] = next
                matrix[t+1][j] = cur
                t += 1
print(ans)