import sys
from collections import deque

def chBipartite(R):
    Q = deque()
    visited[R] = 1
    Q.append(R)

    while Q:
        u = Q.popleft()
        for i in Map[u]:
            if visited[i] == 0:
                Q.append(i)
                visited[i] = -visited[u]
            else:
                if visited[u] == visited[i]:
                    return False
    return True
      
    
input = sys.stdin.readline
K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    Map = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    
    for i in range(E):
        a, b = map(int, input().split())
        Map[a].append(b)
        Map[b].append(a)

    for i in range(1, V+1):
        if visited[i] == 0:
            res = chBipartite(i)
            if not res:
                print("NO")
                break
    if res:
        print("YES")