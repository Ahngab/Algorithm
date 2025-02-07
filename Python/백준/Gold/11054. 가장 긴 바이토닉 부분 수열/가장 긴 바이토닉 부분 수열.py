import sys

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
rev_arr = arr[::-1]
inc = [1]*(N)
dec = [1]*(N)


for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            inc[i] = max(inc[j] + 1, inc[i])
        if rev_arr[i] > rev_arr[j]:
            dec[i] = max(dec[j] + 1, dec[i])

max_ = 0
for i in range(N):
    max_ = max(inc[i] + dec[N-i-1], max_)

print(max_ - 1)