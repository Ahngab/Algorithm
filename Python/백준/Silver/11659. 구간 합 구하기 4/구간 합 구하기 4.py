import sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
sum_ = [0]*(N+1)
sum_[1] = arr[1]

for i in range(1, N+1):
    sum_[i] = sum_[i-1] + arr[i-1]

for i in range(M):
    start, end = map(int, input().split())
    print(sum_[end] - sum_[start-1])