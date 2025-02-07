import sys
from collections import deque

def BFS(x, y):
    global endX, endY

    Q = deque()
    Q.append((x, y))

    while Q:

        dx, dy = Q.popleft()
        if dx == endX and dy == endY:
            return visited[dx][dy]

        cord = [(dx-1, dy-2), (dx+1, dy-2), (dx-2, dy-1), (dx+2, dy-1), (dx-2, dy+1), (dx+2, dy+1), (dx-1, dy+2), (dx+1, dy+2)]

        for i,j in cord:
            if 0 <= i <= (l-1) and 0 <= j <= (l-1) and visited[i][j] == 0:
                visited[i][j] = visited[dx][dy] + 1
                Q.append((i,j))

input = sys.stdin.readline
T = int(input())

for _ in  range(T):
    l = int(input())
    visited = [[0]*l for _ in range(l)]
    startX , startY = map(int, input().split())
    endX, endY = map(int, input().split())
    print(BFS(startX, startY))  