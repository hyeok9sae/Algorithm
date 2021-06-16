# 파도반 수열
T = int(input())
dp = [0]*101
dp[0], dp[1], dp[2] = 0, 1, 1
for i in range(3, 101):
    dp[i] = dp[i-2] + dp[i-3]
for _ in range(T):
    print(dp[int(input())])