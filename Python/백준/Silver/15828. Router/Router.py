import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
Q = deque()
cnt = 0

while True:
    packet = int(input())

    if packet == -1:
        if Q:
            print(*Q, sep = " ")
        else:
            print("empty")
        break

    elif packet == 0:
        Q.popleft()
        cnt -= 1

    elif cnt < N:
        Q.append(packet)
        cnt += 1