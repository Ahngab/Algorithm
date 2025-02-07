import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
deq = deque(enumerate(map(int, input().split())))


while deq:
    idx, num = deq.popleft()
    print(idx+1, end=" ")
    
    if num > 0:
        deq.rotate(-num+1)
    else:
        deq.rotate(-num)