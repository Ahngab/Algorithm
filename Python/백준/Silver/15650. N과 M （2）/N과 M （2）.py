import sys
from itertools import combinations

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [str(i) for i in range(1, N+1)]
arr = combinations(arr, M)

for i in arr:
    print(' '.join(i))