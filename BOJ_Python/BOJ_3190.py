# 뱀
from collections import deque

def is_in(ny, nx):
    if 0 <= ny < N and 0 <= nx < N:
        return True
    return False

def move(row, col):
    sec, d = 0, 0
    deq = deque()
    matrix[row][col] = -1
    deq.append((row, col))
    ny, nx = row, col
    while True:
        ny += dy[d]
        nx += dx[d]
        if not is_in(ny, nx) or matrix[ny][nx] == -1:
            return sec+1
        if matrix[ny][nx] == 0:
            ey, ex = deq.popleft()
            matrix[ey][ex] = 0
        matrix[ny][nx] = -1
        deq.append((ny, nx))
        sec += 1
        if sec in dic:
            if dic[sec] == 'D':
                d = (d+1)%4
            else:
                d = (d-1)%4

N = int(input())
K = int(input())
matrix = [[0]*N for _ in range(N)]
dy, dx = (0, 1, 0, -1), (1, 0, -1, 0)
for _ in range(K):
    a, b = map(int, input().split())
    matrix[a-1][b-1] = 1
L = int(input())
dic = {}
for _ in range(L):
    a, b = map(str, input().split())
    dic[int(a)] = b
print(move(0, 0))