import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [str(i) for i in range(1, N+1)]
arr = combinations_with_replacement(arr, M)

for i in arr:
    print(' '.join(i))