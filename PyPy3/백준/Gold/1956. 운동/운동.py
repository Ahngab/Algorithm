#플로이드
import sys, heapq
INF = 1e9

input = sys.stdin.readline
V, E = map(int, input().split())
graph = [[INF]*(V+1) for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u][v] = min(graph[u][v], w)

for k in range(1, V+1):
    for a in range(1, V+1):
        for b in range(1, V+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

min_ = INF
for i in range(1, V+1):
    for j in range(1, V+1):
        if i == j and graph[i][k] != INF:
            min_ = min(graph[i][j], min_)

if min_ == INF:
    print(-1)
else:
    print(min_)