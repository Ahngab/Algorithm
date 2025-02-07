import sys
from collections import deque

def BFS(R):
    global time

    time += 1
    visited[R] = time
    Q.append(R)
    while Q:
        u = Q.popleft()
        edges[u].sort(reverse=True)
        for i in edges[u]:
            if visited[i] == 0:
                time += 1
                visited[i] = time
                Q.append(i)

input = sys.stdin.readline
N, M, R = map(int, input().split())

Q = deque()
visited = [0] * (N+1)
edges = [[] for _ in range(N+1)]
time = 0

for i in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

BFS(R)

for i in range(1, len(visited)):
    print(visited[i])