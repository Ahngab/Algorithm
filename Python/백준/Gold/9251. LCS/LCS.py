import sys

input = sys.stdin.readline
str1 = input().strip()
str2 = input().strip()
dp = [ [0]*(len(str2)+1) for _ in range(len(str1)+1) ]

for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

max_ = 0
for i in range(len(dp)):
    max_ = max(max_, max(dp[i]))

print(max_)