import sys
from itertools import product

N, M = map(int, input().split())
arr = list(map(str, sorted(list(map(int, input().split())))))

for i in product(arr, repeat = M):
    print(" ".join(i))
