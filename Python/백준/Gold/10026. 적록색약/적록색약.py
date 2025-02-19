from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
board = [list(input().strip()) for _ in range(N)]
visited1 = [[0] * (N) for _ in range(N)]
cnt1 = 0

for a in range(N):
    for b in range(N):
        if visited1[a][b] == 0:
            alph = board[a][b]
            visited1[a][b] = 1
            Q = deque()
            Q.append([a, b])

            while Q:
                x, y = Q.popleft()

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue

                    if board[nx][ny] == alph and visited1[nx][ny] == 0:
                        Q.append([nx, ny])
                        visited1[nx][ny] = 1
            cnt1 += 1

for i in range(N):
    for j in range(N):
        if board[i][j] == "G":
            board[i][j] = "R"
cnt2 = 0
visited2 = [[0] * (N) for _ in range(N)]

for a in range(N):
    for b in range(N):
        if visited2[a][b] == 0:
            alph = board[a][b]
            visited2[a][b] = 1
            Q = deque()
            Q.append([a, b])

            while Q:
                x, y = Q.popleft()

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue

                    if board[nx][ny] == alph and visited2[nx][ny] == 0:
                        Q.append([nx, ny])
                        visited2[nx][ny] = 1
            cnt2 += 1

print(cnt1, cnt2)