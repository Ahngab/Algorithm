import sys
from collections import deque

input = sys.stdin.readline
stack_l = deque(list(input().strip()))
stack_r = deque()

N = int(input())

for _ in range(N):
    order = input().split()
    cmd = order[0]

    if cmd == "L" and stack_l:
        stack_r.appendleft(stack_l.pop())
        
    elif cmd == "D" and stack_r:
        stack_l.append(stack_r.popleft())
    
    elif cmd == "B" and stack_l:
        stack_l.pop()
        
    elif cmd == "P":
        stack_l.append(order[1])

print("".join(stack_l) + "".join(stack_r))