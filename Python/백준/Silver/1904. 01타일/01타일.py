import sys

input = sys.stdin.readline
N = int(input())
dp = [0] * (N+2)
dp[1] = 1
dp[2] = 2

for i in range(3, len(dp)):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746
print(dp[N])