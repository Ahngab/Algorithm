import sys

input = sys.stdin.readline
N, K = map(int, input().split())
arr = list(map(int, input().split()))

part = sum(arr[:K])
max_ = part

for i in range(N-K):
    part += arr[i+K]
    part -= arr[i]
    max_ = max(max_, part)

print(max_)