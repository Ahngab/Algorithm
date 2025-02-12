import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def BFS(x, y, z):
    visited[x][y][z] = 1
    Q = deque()
    Q.append([x, y, z])

    while Q:
        a, b, c = Q.popleft()

        if a == N - 1 and b == M - 1:
            return visited[a][b][c]

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            if graph[nx][ny] == 1 and c == 0:
                visited[nx][ny][1] = visited[a][b][0] + 1
                Q.append([nx, ny, 1])
            
            elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[a][b][c] + 1
                Q.append([nx, ny, c])
    return -1




input = sys.stdin.readline
N, M = map(int, input().split())
graph = []
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

 
for _ in range(N):
    graph.append(list(map(int, input().strip())))

print(BFS(0,0,0))
