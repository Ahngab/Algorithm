import sys
from itertools import combinations_with_replacement

N, M = map(int, input().split())
arr = list(map(str, sorted(list(map(int, input().strip().split())))))
for i in combinations_with_replacement(arr, M):
    print(" ".join(i))