import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(x, y):
    Q.append((x,y))

    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            else:
                if maze[nx][ny] == 1:
                    maze[nx][ny] = maze[x][y] + 1
                    Q.append((nx, ny))

input = sys.stdin.readline
N, M = map(int, input().split())
maze = [list(map(int, list(input().strip()))) for _ in range(N)]
Q = deque()

BFS(0,0)
print(maze[N-1][M-1])

    