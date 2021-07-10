# 연구소
from collections import deque
from itertools import combinations as cb

def count_safezone():
    count = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0 and not visited[i][j]:
                count += 1
    return count

def is_in(ny, nx):
    if 0 <= ny < N and 0 <= nx < M:
        return True
    return False

def install_wall(combi):
    for y, x in combi:
        matrix[y][x] = 1

def uninstall_wall(combi):
    for y, x in combi:
        matrix[y][x] = 0

def virus_diffusion(row, col):
    visited[row][col] = True
    deq = deque()
    deq.append((row, col))
    while deq:
        y, x = deq.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if not is_in(ny, nx):
                continue
            if matrix[ny][nx] != 0 or visited[ny][nx]:
                continue
            visited[ny][nx] = True
            deq.append((ny, nx))

N, M = map(int, input().split())
matrix = list(list(map(int, input().split())) for _ in range(N))
dy, dx = [0, -1, 0, 1], [-1, 0, 1, 0]
lst = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            lst.append((i, j))
combis = cb(lst, 3)
answer = 0
for combi in combis:
    install_wall(combi)
    visited = [[False]*M for _ in range(N)]
    for a in range(N):
        for b in range(M):
            if matrix[a][b] == 2:
                virus_diffusion(a, b)
    # print(*visited, sep="\n")
    # print("-")
    res = count_safezone()
    if answer < res:
        answer = res
    uninstall_wall(combi)
print(answer)