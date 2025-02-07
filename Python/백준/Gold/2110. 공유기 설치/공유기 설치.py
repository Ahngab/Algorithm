import sys

input = sys.stdin.readline
N, c = map(int, input().split())

arr = sorted([int(input()) for _ in range(N)])

start = 1
end = arr[-1] - arr[0]

while start <= end :
    mid = (start + end) // 2
    cnt = 1
    current = arr[0]

    for i in range(1, len(arr)):
        if arr[i] - current >= mid:
            cnt += 1
            current = arr[i]

    if cnt >= c:
        start = mid + 1
        res = mid
    else:
        end = mid - 1

print(res)