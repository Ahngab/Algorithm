import sys, heapq
INF = 1e9

#Dijkstra
def dijkstra(start):
    Q = []
    dist = [INF for _ in range(V+1)]
    dist[start] = 0
    heapq.heappush(Q, [0, start])

    while Q:
        cur_dist, u = heapq.heappop(Q)
        if dist[u] < cur_dist:
            continue
        for v, w in edges[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(Q, [dist[v], v])

    return dist

#Initialize
input = sys.stdin.readline
V, E = map(int, input().split())

edges = [[] for _ in range(V+1)]

for i in range(E):
    u, v, w = map(int, input().split())
    edges[u].append([v, w])
    edges[v].append([u, w])

v1, v2 = map(int, input().split())

#Dist 1 to ohters
dist1toOthers = dijkstra(1)

#Dist v1 to others
distV1toOthers = dijkstra(v1)

#Dist v2 to others
distV2toOthers = dijkstra(v2)

distV1V2End = dist1toOthers[v1] + distV1toOthers[v2] + distV2toOthers[V]
distV2V1End = dist1toOthers[v2] + distV2toOthers[v1] + distV1toOthers[V]

#print(distV1V2End, distV2V1End)
min_ = min(distV1V2End, distV2V1End)

if min_ < INF:
    print(min_)
else:
    print(-1)