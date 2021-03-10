# 파이프 옮기기 1
def dfs(row, col, flag):
    global count
    if row == N-1 and col == N-1:
        count += 1
        return
    if flag == 0:
        if col+1 < N and matrix[row][col+1] == 0:
            dfs(row, col+1, 0)
        if row+1 < N and col+1 < N and matrix[row][col+1] == 0 and matrix[row+1][col] == 0 and matrix[row+1][col+1] == 0:            
            dfs(row+1, col+1, 1)
    elif flag == 1:
        if col+1 < N and matrix[row][col+1] == 0:
            dfs(row, col+1, 0)
        if row+1 < N and col+1 < N and matrix[row][col+1] == 0 and matrix[row+1][col] == 0 and matrix[row+1][col+1] == 0:
            dfs(row+1, col+1, 1)
        if row+1 < N and matrix[row+1][col] == 0:
            dfs(row+1, col, 2)
    else:
        if row+1 < N and col+1 < N and matrix[row][col+1] == 0 and matrix[row+1][col] == 0 and matrix[row+1][col+1] == 0:
            dfs(row+1, col+1, 1)
        if row+1 < N and matrix[row+1][col] == 0:
            dfs(row+1, col, 2)
    return count

N = int(input())
matrix = []
count = 0
dy, dx = [1, 1, 0], [0, 1, 1]
for _ in range(N):
    matrix.append(list(map(int, input().split())))
print(dfs(0, 1, 0))