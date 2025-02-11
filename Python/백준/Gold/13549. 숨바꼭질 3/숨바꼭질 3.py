import sys
from collections import deque

def BFS(R, targetCord):
    Q = deque()
    visited[R] = 0
    Q.append(R)

    while Q:
        u = Q.popleft()

        if u == targetCord:
            return visited[targetCord]

        for i in (2*u, u-1, u+1):
            if 0 <= i <= limit and visited[i] == 0:
                if i == 2*u:
                    visited[i] = visited[u]
                    Q.append(i)
                else:
                    visited[i] = visited[u] + 1
                    Q.append(i)

    

input = sys.stdin.readline
N, K = map(int, input().split())
limit = 100000
visited = [0] * (limit + 1)

time = BFS(N, K)
print(time)
