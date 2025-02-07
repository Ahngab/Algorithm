import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    arr = [0]* (N+4)

    arr[1] = 1
    arr[2] = 1
    arr[3] = 1
    for i in range(4, len(arr)):
        arr[i] = arr[i-3] + arr[i-2]

    print(arr[N])