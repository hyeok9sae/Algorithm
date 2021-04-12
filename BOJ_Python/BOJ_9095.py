# 1, 2, 3 더하기
def solve(sum):
    global cnt
    if sum == n:
        cnt += 1
        return
    if sum > n:
        return
    for i in range(1, 4):
        solve(sum+i)
T = int(input())
for _ in range(T):
    n = int(input())
    cnt = 0
    solve(0)
    print(cnt)