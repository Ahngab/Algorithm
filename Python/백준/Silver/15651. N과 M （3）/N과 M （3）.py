import sys
from itertools import product

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [str(i) for i in range(1, N+1)]
arr = product(arr, repeat = M)
for i in arr:
    print(' '.join(i))