# 다리 만들기 2
from collections import deque

def is_in(ny, nx):
    if 0 <= ny < N and 0 <= nx < M:
        return True
    return False

def bfs(row, col, num):
    visited[row][col] = True
    deq = deque()
    deq.append([row, col])
    while deq:
        y, x = deq.popleft()
        matrix[y][x] = num
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if not is_in(ny, nx):
                continue
            if matrix[ny][nx] == 0 or visited[ny][nx]:
                continue
            visited[ny][nx] = True
            deq.append([ny, nx])

def bridge(row, col):
    standard = matrix[row][col]
    for i in range(4):
        ny, nx = row+dy[i], col+dx[i]
        if not is_in(ny, nx):
            continue
        if matrix[ny][nx] != 0:
            continue
        dist = 0
        while True:
            if not is_in(ny, nx):
                break
            if matrix[ny][nx] != 0 and matrix[ny][nx] != standard:
                if dist > 1:
                    lst.add((standard, matrix[ny][nx], dist))
                break
            if matrix[ny][nx] == standard:
                break
            ny += dy[i]
            nx += dx[i]
            dist += 1

def make_set(num):
    parent[num] = num
    rank[num] = 0

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(v1, v2):
    root1 = find(v1)
    root2 = find(v2)
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

def kruskal(lst):
    mst = []
    for num in range(1, number):
        make_set(num)
    lst = list(lst)
    lst.sort(key=lambda x:x[2])
    for v1, v2, distance in lst:
        if find(v1) != find(v2):
            union(v1, v2)
            mst.append((v1, v2, distance))
    return mst

N, M = map(int, input().split())
matrix = list(list(map(int, input().split())) for _ in range(N))
visited = [[False]*M for _ in range(N)]
dy, dx = [0, -1, 0, 1], [-1, 0, 1, 0]
number = 1
lst = set()
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1 and not visited[i][j]:
            bfs(i, j, number)
            number += 1
for i in range(N):
    for j in range(M):
        if matrix[i][j] != 0:
            bridge(i, j)
parent, rank = {}, {}
res = kruskal(lst)
answer = 0
temp = set()
for i in parent:
    temp.add(find(i))
if len(temp) > 1:
    answer = -1
else:
    for i in res:
        answer += i[2]
print(answer)