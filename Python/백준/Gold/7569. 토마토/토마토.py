import sys
from collections import deque

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def BFS():

    while Q:
        x, y, z = Q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and box[nz][ny][nx] == 0:
                box[nz][ny][nx] = box[z][y][x] + 1
                Q.append((nx, ny, nz))
        


input = sys.stdin.readline
N, M, H = map(int, input().split())

box = [ [list(map(int, input().split())) for _ in range(M) ] for _ in range(H)]
Q = deque()

for i in range(N):
    for j in range(M):
        for k in range(H):
            if box[k][j][i] == 1:
                Q.append((i, j, k))

BFS()
flag = 0
max_ = -1
for i in box:
    for j in i:
        if 0 in j:
            flag = 1
      
            break
        max_ = max(max(j), max_)
if flag:
    print(-1)
else:
    print(max_-1)