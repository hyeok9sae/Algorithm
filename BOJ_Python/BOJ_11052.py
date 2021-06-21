# 카드 구매하기
N = int(input())
cost = [0] + list(map(int, input().split()))
dp = [0]*(N+1)
dp[1] = cost[1]
dp[2] = max(cost[2], cost[1]*2)
for i in range(3, N+1):
    dp[i] = cost[i]
    for j in range(1, N):
        dp[i] = max(dp[i], dp[j]+dp[i-j])
print(dp[N])