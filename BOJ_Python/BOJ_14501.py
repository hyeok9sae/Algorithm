# 퇴사
def solve(start, sum):
    global ans
    if start == N+1:
        if ans < sum:
            ans = sum
        return
    if start > N+1:
        return

    solve(start+1, sum)
    solve(start+T[start], sum+P[start])

N = int(input())
T, P = [0], [0]
for _ in range(N):
    a, b = map(int, input().split())
    T.append(a)
    P.append(b)
ans = float('-inf')
solve(1, 0)
print(ans)