import sys
INF = 1e9

input = sys.stdin.readline
V = int(input())
E = int(input())

graph = [[INF]*(V+1) for _ in range(V+1)]

for i in range(1, V+1):
    for j in range(1, V+1):
        if i == j:
            graph[i][j] = 0

for _ in range(E):
    i, j, c = map(int, input().split())
    graph[i][j] = min(c, graph[i][j])

for k in range(1, V+1):
    for a in range(1, V+1):
        for b in range(1, V+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, V+1):
    for j in range(1, V+1):
        if graph[i][j] == INF:
            print(0, end = ' ')
        else:
            print(graph[i][j], end = ' ')
    print()