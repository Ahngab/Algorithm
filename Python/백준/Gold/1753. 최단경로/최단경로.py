import sys
import heapq
INF = int(1e9)

def dijkstra(R):
    Q = []
    heapq.heappush(Q, (0, R))
    dist[R] = 0

    while Q:
        cur_dist, u = heapq.heappop(Q)
        if cur_dist > dist[u]: #중복확인
            continue
        
        for v, weight  in edges[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(Q, (dist[v], v))

input = sys.stdin.readline
V, E = map(int, input().split())
R = int(input())

dist = [INF] * (V+1)
edges = [[] for _ in range(V+1)]

for i in range(E):
    u, v, w = map(int, input().split())
    edges[u].append((v, w))

dijkstra(R)
for i in dist[1:]:
    if i == INF:
        print("INF")
    else:
        print(i)