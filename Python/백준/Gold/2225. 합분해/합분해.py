N, K = map(int, input().split())
answer = 0
dp = [[0] * (K+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(N + 1):
    for j in range(1, K + 1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[N][K] % 1000000000)