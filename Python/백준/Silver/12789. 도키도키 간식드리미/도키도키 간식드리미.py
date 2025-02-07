import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
arr = deque((map(int, input().split())))
stack = deque()
index = 1

for i in arr:
    stack.append(i)

    while stack and stack[-1] == index:
        stack.pop()
        index += 1

if len(stack) != 0:
    print("Sad")
else:
    print("Nice")