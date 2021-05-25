# 드래곤 커브
def is_in(ny, nx):
    if 0 <= ny < 101 and 0 <= nx < 101:
        return True
    return False

def check(row, col):
    if not is_in(row, col+1) or not is_in(row+1, col) or not is_in(row+1, col+1):
        return False
    if matrix[row][col+1] == 0 or matrix[row+1][col] == 0 or matrix[row+1][col+1] == 0:
        return False
    return True

def curve(y, x, d, g):
    lst = [d]
    matrix[y][x] = 1
    for i in range(g):
        tmp = []
        for j in range(len(lst)-1, -1, -1):
            tmp.append((lst[j]+1)%4)
        lst += tmp
    # print(lst)
    for i in lst:
        y, x = y + dy[i], x + dx[i]
        matrix[y][x] = 1

N = int(input())
matrix = [[0]*(101) for _ in range(101)]
dy, dx = [0, -1, 0, 1], [1, 0, -1, 0]
for _ in range(N):
    x, y, d, g = map(int, input().split())
    curve(y, x, d, g)
ans = 0
for i in range(101):
    for j in range(101):
        if matrix[i][j] == 1 and check(i, j):
            ans += 1
print(ans)
# print(*matrix, sep="\n")
# print(matrix[46][31])