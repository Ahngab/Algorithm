from collections import deque

def BFS(start):
    visited[start] = 1
    Q = deque()
    Q.append([start, ''])

    while Q:
        n, op = Q.popleft()

        if n == B:
            return op

        D = (2*n) % 10000
        if not visited[D]:
            visited[D] = 1
            Q.append([D, op + "D"])

        S = (n -1) % 10000
        if not visited[S]:
            visited[S] = 1
            Q.append([S, op + "S"])

        L = n//1000 + (n%1000) * 10
        if not visited[L]:
            visited[L] = 1
            Q.append([L, op + "L"])

        R = n//10 + (n % 10) *1000
        if not visited[R]:
            visited[R] = 1
            Q.append([R, op + "R"])



T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    visited = [0] * 10001
    print(BFS(A))