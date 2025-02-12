import sys
from collections import deque


input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
NGE = [-1] * len(arr)
stack = deque()
stack.append(0)

for i in range(len(arr)):
    while stack and arr[i] > arr[stack[-1]]:
        NGE[stack.pop()] = arr[i]

    stack.append(i)

print(*NGE, sep=" ")
#    i love you
