import sys
from collections import deque

def Virus(R):
    global cnt

    infected[R] = 1
    Q.append(R)
    
    while Q:
        u = Q.popleft()
        for i in connect[u]:
            if infected[i] == 0:
                cnt += 1
                infected[i] = 1
                Q.append(i)

input = sys.stdin.readline                 
N = int(input())
M = int(input())
cnt = 0
connect = [[] for _ in range(N+1)]
infected = [0] * (N+1)
Q = deque()
                        

for i in range(M):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)

Virus(1)
print(cnt)