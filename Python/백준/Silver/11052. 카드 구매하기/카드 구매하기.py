N = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)
dp[1] = arr[1]

for i in range(1, N + 1):
    for j in range(i+1):
        dp[i] = max(dp[i], dp[j] + arr[i - j])

print(dp[N])