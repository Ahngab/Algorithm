import sys
from itertools import combinations

input = sys.stdin.readline
while True:
    T = list(input().split())
    k = int(T[0])
    if k == 0: break
    arr = T[1:]

    for i in combinations(arr, 6):
        print(" ".join(i))
    print()




