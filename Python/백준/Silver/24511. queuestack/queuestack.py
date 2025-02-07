import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
qs = list(map(int, input().split()))
element = list(map(int, input().split()))
deq = deque()

for i in range(N):
    if qs[i] == 0:
        deq.append(element[i])

M = int(input())
C = list(map(int, input().split()))

for i in range(M):
    deq.appendleft(C[i])
    print(deq.pop(), end=" ")

