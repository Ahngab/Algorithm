import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS():

    while Q:
        x, y = Q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M  and box[ny][nx] == 0:
                box[ny][nx] = box[y][x] + 1
                Q.append((nx, ny))
        


input = sys.stdin.readline
N, M = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(M) ]
Q = deque()

for i in range(N):
    for j in range(M):
        if box[j][i] == 1:
            Q.append((i, j))

BFS()
flag = 0
max_ = -1
for i in box:
    if 0 in i:
        flag = 1
        break
    max_ = max(max(i), max_)
if flag:
    print(-1)
else:
    print(max_-1)