import sys
from collections import deque


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(x, y):
    global N, M

    visited[x][y] = 0
    Q.append((x,y))

    while Q:
        x, y = Q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue
            else:
                if visited[nx][ny] == 1:
                    visited[nx][ny] = 0
                    Q.append((nx, ny))

input = sys.stdin.readline
T = int(input())
    
for _ in range(T):
    cnt = 0
    Q = deque()
    M, N, K = map(int, input().split())
    visited = [[0]*N for _ in range(M)]
    
    for i in range(K):
        a, b = map(int, input().split())
        visited[a][b] = 1

    for i in range(M):
        for j in range(N):
            if visited[i][j] == 1:
                BFS(i, j)
                cnt += 1
    print(cnt)