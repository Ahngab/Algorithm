import heapq, sys
INF = 1e9

N = int(input())
graph = [[INF]*N for _ in range(N)]
board = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            graph[i][j] = 1

for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(N):
    for j in range(N):
        if graph[i][j] == INF:
            print(0, end= " ")
        else:
            print(1, end = " ")
    print()