# 상어 초등학교
from collections import deque

def is_in(ny, nx):
    if 0 <= ny < N and 0 <= nx < N:
        return True
    return False

def solve(v):
    deq = deque([])
    max_cnt = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] != 0:
                continue
            cnt = 0
            for k in range(4):
                ny, nx = i + dy[k], j + dx[k]
                if not is_in(ny, nx):
                    continue
                if matrix[ny][nx] in lst[v][1:]:
                    cnt += 1
            if max_cnt <= cnt:
                if max_cnt < cnt:
                    max_cnt = cnt
                    deq = deque([])
                deq.append((i, j))
    if len(deq) > 1:
        solve2(deq, v)
    else:
        y, x = deq.popleft()
        matrix[y][x] = lst[v][0]

def solve2(deq, v):
    max_cnt = 0
    deq2 = deque([])
    while deq:
        y, x = deq.popleft()
        cnt = 0
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not is_in(ny, nx):
                continue
            if matrix[ny][nx] == 0:
                cnt += 1
        if max_cnt <= cnt:
                if max_cnt < cnt:
                    max_cnt = cnt
                    deq2 = deque([])
                deq2.append((y, x))
    if len(deq2) > 1:
        solve3(deq2, v)
    else:
        a, b = deq2.popleft()
        matrix[a][b] = lst[v][0]

def solve3(deq2, v):
    y, x = deq2.popleft()
    deq3 = deque([(y, x)])
    while deq2:
        ny, nx = deq2.popleft()
        if y < ny:
            continue
        elif y == ny:
            deq3.append((ny, nx))
        else:
            deq3 = deque([(ny, nx)])
    if len(deq3) > 1:
        solve4(deq3, v)
    else:
        a, b = deq3.popleft()
        matrix[a][b] = lst[v][0]

def solve4(deq3, v):
    y, x = deq3.popleft()
    deq4 = deque([(y, x)])
    while deq3:
        ny, nx = deq3.popleft()
        if x < nx:
            continue
        else:
            deq4 = deque([(ny, nx)])
    a, b = deq4.popleft()
    matrix[a][b] = lst[v][0]

def res(row, col):
    cnt = 0
    for i in range(4):
        ny = row + dy[i]
        nx = col + dx[i]
        if not is_in(ny, nx):
            continue
        if matrix[ny][nx] in dic[matrix[row][col]]:
            cnt += 1
    # print(cnt)
    return cnt

N = int(input())
dic = {}
lst = []
matrix = [[0]*N for _ in range(N)]
dy, dx = [0, -1, 0, 1], [-1, 0, 1, 0]
for i in range(N*N):
    lst.append(list(map(int, input().split())))
    dic[lst[i][0]] = lst[i][1:]
    solve(i)
ans = 0
for i in range(N):
    for j in range(N):
        num = res(i, j)
        if num == 0:
            ans += 0
        elif num == 1:
            ans += 1
        elif num == 2:
            ans += 10
        elif num == 3:
            ans += 100
        else:
            ans += 1000
print(ans)