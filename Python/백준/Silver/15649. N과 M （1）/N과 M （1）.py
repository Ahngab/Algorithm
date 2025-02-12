import sys
from itertools import permutations

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [str(i) for i in range(1, N+1)]
arr = permutations(arr, M)

for i in arr:
    print(' '.join(i))