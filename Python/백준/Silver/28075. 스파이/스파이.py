import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
arr = []
for _ in range(2):
    arr.extend(list(map(int, input().split())))

answer = 0

def work(n, nowM, beforePlace):
    global answer
    if n > N:
        return 

    if n == N:
        if nowM >= M:
            answer += 1
        return
    
    for i in range(6):
        if i % 3 == beforePlace:
            work(n+1, nowM + arr[i]//2, i % 3)
        else:
            work(n+1, nowM + arr[i], i % 3)

work(0, 0, 4)
print(answer)