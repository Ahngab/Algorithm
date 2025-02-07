import sys
from collections import deque

N, M = map(int, input().split())
ladder = {}
snake  = {}
visited = [0] * 101
Q = deque()

for i in range(N):
    start, end = map(int, input().split())
    ladder[start] = end

for i in range(M):
    start, end = map(int, input().split())
    snake[start] = end

Q.append(1)
visited[1] = 1
cnt = 1

while Q:
    x = Q.popleft()

    if x == 100:
        print(visited[x] - 1)
        break
    for i in range(1, 7):
        nx = x + i
        
        if nx <= 100 and visited[nx] == 0:
            if nx in ladder:
                nx = ladder[nx]

            elif nx in snake:
                nx = snake[nx]
            
            if visited[nx] == 0:
                visited[nx] = visited[x] + 1
                Q.append(nx)
            