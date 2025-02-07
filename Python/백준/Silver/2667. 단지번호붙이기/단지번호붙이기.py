import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def BFS(x, y):
    global N

    cnt = 1

    house[x][y] = 1
    Q.append((x, y))

    while Q:
        x, y = Q.popleft()

        house[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            else:
                if house[nx][ny] == 1:
                    Q.append((nx, ny))
                    house[nx][ny] = 0
                    cnt += 1
    return cnt



N = int(input())
house = [list(map(int, list(input().strip()))) for _ in range(N)]
Q = deque()
res = []


for i in range(N):
    for j in range(N):
        if house[i][j] == 1:
            res.append(BFS(i, j))

print(len(res))
for i in sorted(res):
    print(i)
