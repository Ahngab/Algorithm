from collections import deque
INF = 1e9

N, M = map(int, input().split())
graph = [[INF]*(N + 1) for _ in range(N+1)]

for _  in range(M):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

for i in range(1, N + 1):
    graph[i][i] = 0

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

answer = []

for i in range(1, N+1):
    answer.append(sum(graph[i][1:]))

print(answer.index(min(answer)) + 1)