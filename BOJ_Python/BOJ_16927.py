# 배열 돌리기 2
def solve():
    tmps = []
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
        tmps.append(tmp)
    for k in range(gn):
        idx = R%len(tmps[k])
        for i in range(k, M-k-1):
            A[k][i] = tmps[k][idx]
            idx = (idx+1)%len(tmps[k])
        for i in range(k, N-k-1):
            A[i][M-k-1] = tmps[k][idx]
            idx = (idx+1)%len(tmps[k])
        for i in range(M-k-1, k, -1):
            A[N-k-1][i] = tmps[k][idx]
            idx = (idx+1)%len(tmps[k])
        for i in range(N-k-1, k, -1):
            A[i][k] = tmps[k][idx]
            idx = (idx+1)%len(tmps[k])
        # print(*A, sep="\n")

N, M, R = map(int, input().split())
A = list(list(map(int, input().split())) for _ in range(N))
gn = min(N, M)//2
solve()
for i in A:
    print(*i)