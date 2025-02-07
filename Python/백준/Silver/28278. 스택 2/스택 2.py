from collections import deque
import sys

N = int(sys.stdin.readline())
stack = deque()

for _ in range(N):
    order = list(map(int, sys.stdin.readline().strip().split()))

    if order[0] == 1:
        stack.append(order[1])
    
    elif order[0] == 2:
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    
    elif order[0] == 3:
        print(len(stack))
    
    elif order[0] == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    
    elif order[0] == 5:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
        