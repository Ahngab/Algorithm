import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()

for _ in range(N):
    order = sys.stdin.readline().strip().split()

    if order[0] == "push":
        queue.append(int(order[1]))
    
    elif order[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    
    elif order[0] == "size":
        print(len(queue))

    elif order[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    
    elif order[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    
    elif order[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])