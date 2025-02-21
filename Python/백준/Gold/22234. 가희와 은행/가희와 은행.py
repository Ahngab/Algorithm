import sys
from collections import deque

input = sys.stdin.readline
N, T, W = map(int, input().split())
Q = deque([list(map(int, input().split())) for _ in range(N)])
M = int(input())
delay = deque(sorted([list(map(int, input().split())) for _ in range(M)], key = lambda x: x[2]))
w = 0
time = 0

while Q:
    id, t = Q.popleft()

    if T >= t:
        time += t
        while delay and delay[0][2] <= time:
            iD, tt, _ = delay.popleft()
            Q.append([iD, tt])
        for _ in range(t):
            w += 1
            if w == W + 1:
                break
            print(id)

    else:
        time += T
        while delay and delay[0][2] <= time:
            iD, tt, _ = delay.popleft()
            Q.append([iD, tt])
        Q.append([id, t - T])
        for _ in range(T):
            w += 1
            if w == W + 1:
                break
            print(id)

    if w == W + 1:
        break

    
    