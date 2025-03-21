import sys

input = sys.stdin.readline
N = int(input())

dp = [0]*(N+1)
step = [0] * (N+1)

for i in range(1, N+1):
    step[i] = int(input())

if N == 1:
    print(step[1])

elif N == 2:
    print(step[2] + step[1])

else:
    dp[1] = step[1]
    dp[2] = step[1] + step[2]

    for i in range(3, N+1):
        dp[i] = max(dp[i-2] + step[i], dp[i-3] + step[i-1] + step[i])

    print(dp[N])