import sys

n = 11
dp = [0] * (n + 1)
dp[:4] = [0, 1, 2, 4]

for i in range(4, n + 1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

T = int(input())

for _ in range(T):
    n = int(input())
    print(dp[n])