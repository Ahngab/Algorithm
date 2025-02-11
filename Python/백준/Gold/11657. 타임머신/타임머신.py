import sys, heapq
INF = 1e9

def bellmanFord(R):
    dist[R] = 0

    for i in range(V+1):
        for j in range(E):
            u, v, w = edges[j][0], edges[j][1], edges[j][2]
            
            if dist[u] != INF and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                if i == V:
                    return True
    return False

input = sys.stdin.readline
V, E = map(int, input().split())
dist = [INF for _ in range(V+1)]
edges = []

for i in range(E):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

result = bellmanFord(1)

if result:
    print(-1)

else:
    for i in dist[2:]:
        if i == INF:
            print(-1)
        else:
            print(i)