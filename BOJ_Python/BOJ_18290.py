# NM과 K (1)
def init(ny, nx):
    if 0 <= ny < N and 0 <= nx < M:
        return True
    else:
        return False

def comb(px, py, r, sum):
    if r == K:
        global max
        if max < sum:
            max = sum
        return
    for i in range(px, N):
        for j in range(py if i == px else 0, M):
            if visited[i][j]:
                continue
            check = True
            for k in range(4):
                ny = i + dy[k]
                nx = j + dx[k]
                if not init(ny, nx):
                    continue
                if visited[ny][nx]:
                    check = False
            if check:
                visited[i][j] = True
                comb(i, j, r+1, sum+matrix[i][j])
                visited[i][j] = False
                    
N, M, K = map(int, input().split())
dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]
ans = []
max = float('-inf')
matrix = [[*map(int, input().split())] for _ in range(N)]
visited = [[False]*M for _ in range(N)]
comb(0, 0, 0, 0)
print(max)