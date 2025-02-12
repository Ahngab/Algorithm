import sys
from itertools import product

input = sys.stdin.readline
N, K = map(int, input().split())
K = len(str(N))
arr = list(input().split())
possible = []

max_ = 0

for i in range(1, K+1):
    for j in product(arr, repeat=i):
        num = int(''.join(j))
        if num <= N:
            max_ = max(num, max_)
print(max_)