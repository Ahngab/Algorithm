import sys, heapq
INF = 1e9

def dijkstra(R):
    Q = []
    dist = [INF for _ in range(V+1)]
    dist[R] = 0
    heapq.heappush(Q, [0, R])

    while Q:
        cur_dist, u = heapq.heappop(Q)

        if dist[u] < cur_dist:
            continue

        for v, w in edges[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(Q, [dist[v], v])
    return dist

input = sys.stdin.readline
T = int(input())

for _ in range(T):

    V, E, t = map(int, input().split())
    s, g, h = map(int, input().split())
    edges = [[] for _ in range(V+1)]

    for _ in range(E):
        u, v, w = map(int, input().split())
        edges[u].append([v, w])
        edges[v].append([u, w])
    
    target = [int(input()) for _ in range(t)]

    #Start to Others
    distFromStart = dijkstra(s)

    #H to Others
    distFromH = dijkstra(h)

    #G to Others
    distFromG = dijkstra(g)

    answer = []
    for t in target:
        directDist2target = distFromStart[t]
        withGH2target = distFromStart[g] + distFromG[h] + distFromH[t]
        withHG2target = distFromStart[h] + distFromH[g] + distFromG[t]

        if directDist2target == withGH2target or directDist2target == withHG2target:
            answer.append(t)

    print(*sorted(answer))


    
