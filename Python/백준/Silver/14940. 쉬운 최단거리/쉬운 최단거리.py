from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def BFS(x, y):
    visited[x][y] = 0
    Q = deque()
    Q.append([x, y])

    while Q:
        x, y = Q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            else:
                if board[nx][ny] != 0 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    Q.append([nx, ny])
                


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1]*M for i in range(N)]


for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            x = i
            y = j
        elif board[i][j] == 0:
            visited[i][j] = 0


BFS(x, y)
for i in visited:
    print(*i, sep=" ")
