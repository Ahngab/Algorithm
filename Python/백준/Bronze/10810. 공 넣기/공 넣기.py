N, M = map(int, input().split())
arr = [0]*N

for i in range(M):
    start, end, num = map(int, input().split())
    arr[start-1:end] = [num]*(end - start + 1)

print(*arr)