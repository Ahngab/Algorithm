import sys

limit = 1000000
dp = [1] * (limit + 1)
dp[0] = 0

for i in range(2, limit+1):
    for j in range(1, limit//i + 1):
        dp[i*j] += i
        
    dp[i] = dp[i-1] + dp[i]

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    print(dp[int(input())])