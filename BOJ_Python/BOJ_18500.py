# 미네랄 2
from collections import deque

def throw(idx, row):
    if idx%2 == 0:
        for col in range(C):
            if matrix[row][col] == 'x':
                matrix[row][col] = '.'
                return
    else:
        for col in range(C-1, -1, -1):
            if matrix[row][col] == 'x':
                matrix[row][col] = '.'
                return

def check(row, col):
    visited[row][col] = True
    deq, temp = deque(), []
    deq.append((row, col))
    temp.append([row, col])
    while deq:
        y, x = deq.popleft()
        if y == R-1:
            return
        for i in range(4):
            ny, nx = dy[i]+y, dx[i]+x
            if not is_in(ny, nx):
                continue
            if matrix[ny][nx] == '.' or visited[ny][nx]:
                continue
            visited[ny][nx] = True
            deq.append((ny, nx))
            temp.append([ny, nx])
    drop(temp)

def is_in(ny, nx):
    if 0 <= ny < R and 0 <= nx < C:
        return True
    return False

def drop(temp):
    # print(temp)
    min_k = float('inf')
    temp.sort(key=lambda x:x[0], reverse=True)
    # print(temp)
    for y, x in temp:
        if matrix[y+1][x] == 'x':
            continue
        k = 1
        while True:
            if y+k >= R or (matrix[y+k][x] == 'x' and not visited[y+k][x]):
                break 
            k += 1
        if min_k > k-1:
            min_k = k-1
        # print(min_k)
    for y, x in temp:
        matrix[y+min_k][x] = 'x'
        matrix[y][x] = '.'
    global flag
    flag = True
    
def draw():
    for mat in matrix:
        for m in mat:
            print(m, end="")
        print()

R, C = map(int, input().split())
matrix = [list(input()) for _ in range(R)]
N, bars = int(input()), map(int, input().split())
dy, dx = [0, -1, 0, 1], [-1, 0, 1, 0]
for idx, height in enumerate(bars):
    throw(idx, R-height)
    flag = False
    visited = [[False]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if matrix[r][c] == 'x' and not visited[r][c]:
                visited = [[False]*C for _ in range(R)]
                # print(idx, r, c)
                check(r, c)
                if flag:
                    break
        if flag:
            break
    # draw()
draw()