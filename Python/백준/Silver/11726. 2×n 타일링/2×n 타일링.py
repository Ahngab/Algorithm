from collections import deque

N = int(input())
dp = [0] * (N+1)
dp[0:2] = [1, 1]

for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N]%10007)