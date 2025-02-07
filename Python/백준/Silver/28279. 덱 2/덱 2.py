import sys
from collections import deque

def isEmpty(deq):
    if len(deq) == 0:
        return True
    else:
        return False

N = int(sys.stdin.readline())
deq = deque()

for _ in range(N):
    order = list(map(int, sys.stdin.readline().strip().split()))

    if order[0] == 1:
        deq.appendleft(order[1])

    elif order[0] == 2:
        deq.append(order[1])

    elif order[0] == 3:
        if isEmpty(deq):
            print(-1)

        else:
            print(deq.popleft())

    elif order[0] == 4:
        if isEmpty(deq):
            print(-1)

        else:
            print(deq.pop())

    elif order[0] == 5:
        print(len(deq))

    elif order[0] == 6:
        if isEmpty(deq):
            print(1)
        else:
            print(0)

    elif order[0] == 7:
        if isEmpty(deq):
            print(-1)
        else:
            print(deq[0])

    elif order[0] == 8:
        if isEmpty(deq):
            print(-1)
        else:
            print(deq[-1])