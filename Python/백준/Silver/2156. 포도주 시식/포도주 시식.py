import sys

n = int(input())
cup = [int(input()) for _ in range(n)]
dp = [0] * (n+1)


if n == 1:
    print(cup[0])

elif n == 2:
    print(cup[0] + cup[1])

elif n == 3:
    print(max(cup[0] + cup[1], cup[0] + cup[2], cup[1] + cup[2]))

else:
    dp[0] = cup[0]
    dp[1] = cup[1] + cup[0]
    dp[2] = max(cup[0] + cup[1], cup[0] + cup[2], cup[1] + cup[2])

    for i in range(3, n):
        dp[i] = max(cup[i-1] + dp[i-3]+ cup[i], dp[i-2]+ cup[i], dp[i-1]) 

    print(max(dp))
