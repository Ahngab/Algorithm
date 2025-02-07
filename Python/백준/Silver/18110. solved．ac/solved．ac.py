import sys
from collections import deque

def Round(n):
    N = int(n)

    if n - N >= 0.5:
        return N+1
    else:
        return N

input = sys.stdin.readline
n = int(input())

if n == 0:
    print(0)
else:
    num = Round(n * 0.15)
    arr = sorted([int(input()) for _ in range(n)])

    arr = arr[num:n-num]

    if arr:
        print(Round(sum(arr)/len(arr)))
    else:
        print(0)