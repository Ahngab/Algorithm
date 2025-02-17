import sys
from itertools import permutations

N = int(input())
arr = [str(i) for i in range(1, N+1)]
for i in permutations(arr, N):
    print(" ".join(i))