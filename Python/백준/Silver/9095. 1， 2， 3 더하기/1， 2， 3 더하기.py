import heapq, sys

def find(n, N):
    global answer
    if n == N:
        answer +=1
    
    for i in range(1, 4):
        if n + i <= N:
            find(n + i, N)




T = int(input())

for _ in range(T):
    N = int(input())
    answer = 0
    find(0, N)
    print(answer)