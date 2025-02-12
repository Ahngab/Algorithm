import sys
from collections import deque

input = sys.stdin.readline
string = input().strip()
bomb = input().strip()
length = len(bomb)
stack = []

for i in string:
    stack.append(i)

    if ''.join(stack[len(stack)-length:len(stack)]) == bomb:
        for _ in range(length):
            stack.pop()
        
if stack:
    print(*stack, sep="")

else:
    print("FRULA")