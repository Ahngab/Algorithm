from collections import deque

N, M = map(int, input().split())
campus = [list(input().strip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

Q = deque()
cnt = 0

for i in range(N):
    for j in range(M):
        if campus[i][j] == "I":
            start_x, start_y = i, j

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited[start_x][start_y] = 1
Q.append([start_x, start_y])

while Q:
    x, y = Q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        if visited[nx][ny] == 0:
            if campus[nx][ny] == "P":
                cnt += 1
                Q.append([nx, ny])

            elif campus[nx][ny] == "O":
                Q.append([nx, ny])
            
            visited[nx][ny] = 1

if cnt:
    print(cnt)
else:
    print("TT")
