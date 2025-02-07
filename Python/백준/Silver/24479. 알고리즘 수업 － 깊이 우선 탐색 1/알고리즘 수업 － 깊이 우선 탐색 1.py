import sys

def DFS(node):
    global time

    time += 1
    visited[node] = time
    edges[node].sort()
    for i in edges[node]:
        if visited[i] == 0:
            DFS(i)


sys.setrecursionlimit(150000)
input = sys.stdin.readline
N, M, R = map(int, input().split())

visited = [0]*(N+1)
edges = [[] for _ in range(N+1)]
time = 0

for i in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)


DFS(R)
for i in range(1, len(visited)):
    print(visited[i])