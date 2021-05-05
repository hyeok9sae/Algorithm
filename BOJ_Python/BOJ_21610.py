# 마법사 상어와 비바라기
from collections import deque

def is_in(y, x):
    if 0 <= y < N and 0 <= x < N:
        return True
    return False

N, M = map(int, input().split())
matrix = list(list(map(int, input().split())) for _ in range(N))
visited = [[False]*N for _ in range(N)]
dy = [0,-1,-1,-1,0,1,1,1]
dx = [-1,-1,0,1,1,1,0,-1]
deq = deque([])
deq.append((N-1, 0))
deq.append((N-1, 1))
deq.append((N-2, 0))
deq.append((N-2, 1))
# print(deq)
for _ in range(M):
    d, s = map(int, input().split())
    deq_size = len(deq)
    for _ in range(deq_size):
        y, x = deq.popleft()
        # print(y, x)
        ny = (y + dy[d-1]*s)%N
        nx = (x + dx[d-1]*s)%N
        deq.append((ny, nx))
        # print(ny, nx)
        matrix[ny][nx] += 1
    while deq:
        y, x = deq.popleft()
        cnt = 0
        for i in range(1, 8, 2):
            ty = y + dy[i]
            tx = x + dx[i]
            if not is_in(ty, tx):
                continue
            if matrix[ty][tx] == 0:
                continue
            cnt += 1
        matrix[y][x] += cnt
        visited[y][x] = True
    for i in range(N):
        for j in range(N):
            if matrix[i][j] >= 2 and not visited[i][j]:
                deq.append((i, j))
                matrix[i][j] -= 2
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                visited[i][j] = False
ans = 0
for i in matrix:
    ans += sum(i)
print(ans)