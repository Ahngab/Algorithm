import sys
from collections import deque

def DFS(V):
    print(V, end = " ")
    visited[V] = 1
    edges[V].sort()
    for i in edges[V]:
        if visited[i] == 0:
            DFS(i)

def BFS(V):
    visited[V] = 1
    Q.append(V)

    while Q:
        u = Q.popleft()
        print(u, end= " ")
        edges[u].sort()
        for i in edges[u]:
            if visited[i] == 0:
                visited[i] = 1
                Q.append(i)

input = sys.stdin.readline
sys.setrecursionlimit(150000)
N, M, V = map(int, input().split())
edges = [[] for _ in range(N+1)]
Q = deque()

for i in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

#DFS
visited = [0]*(N+1)
DFS(V)

print()

#BFS
visited = [0]*(N+1)
BFS(V)