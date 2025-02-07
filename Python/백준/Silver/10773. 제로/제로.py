from collections import deque
import sys

K = int(sys.stdin.readline())
stack = deque()

for _ in range(K):
    N = int(sys.stdin.readline())

    if N != 0:
        stack.append(N)

    else:
        stack.pop()
    
print(sum(stack))