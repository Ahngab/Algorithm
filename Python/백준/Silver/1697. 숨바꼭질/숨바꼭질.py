import sys
from collections import deque


def BFS(R):
    global maxCord

    Q = deque()
    Q.append(R)
    
    while Q:
        cord = Q.popleft()

        if cord == K:
                return Map[K]
        
        for i in (cord-1, cord+1, cord*2):
            if i >= 0 and i <= maxCord and Map[i] == 0:
                Map[i] = Map[cord] + 1
                Q.append(i)

input = sys.stdin.readline                
N, K = map(int, input().split())

maxCord = max(N, K)*2
Map = [0]*(maxCord+1)


print(BFS(N))
