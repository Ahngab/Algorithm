import sys
from collections import deque

def BFS(start):
    visited[start] = 1
    Q = deque()
    Q.append(start)

    while Q:
        u = Q.popleft()

        for i in edges[u]:
            if visited[i] == 0:
                visited[i] = 1
                Q.append(i)

input = sys.stdin.readline
N, M = map(int, input().split())
visited = [0] *(N+1)
edges = [[] for _ in range(N+1)]
cnt = 0

for i in range(M):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

for i in range(1, N+1):
    if visited[i] == 0:
        BFS(i)
        cnt += 1


print(cnt)