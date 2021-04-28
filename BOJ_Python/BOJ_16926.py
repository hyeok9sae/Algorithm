# 배열 돌리기 1
def solve():
    idx = 1
    for k in range(gn):
        tmp = []
        for i in range(k, M-k-1):
            tmp.append(A[k][i])
        for i in range(k, N-k-1):
            tmp.append(A[i][M-k-1])
        for i in range(M-k-1, k, -1):
            tmp.append(A[N-k-1][i])
        for i in range(N-k-1, k, -1):
            tmp.append(A[i][k])
        # print(tmp)
    
        for i in range(k, M-k-1):
            A[k][i] = tmp[idx]
            idx = (idx+1)%len(tmp)
        for i in range(k, N-k-1):
            A[i][M-k-1] = tmp[idx]
            idx = (idx+1)%len(tmp)
        for i in range(M-k-1, k, -1):
            A[N-k-1][i] = tmp[idx]
            idx = (idx+1)%len(tmp)
        for i in range(N-k-1, k, -1):
            A[i][k] = tmp[idx]
            idx = (idx+1)%len(tmp)
        # print(*A, sep="\n")

N, M, R = map(int, input().split())
A = list(list(map(int, input().split())) for _ in range(N))
gn = min(N, M)//2
for _ in range(R):
    solve()
for i in A:
    print(*i)