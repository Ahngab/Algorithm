N = int(input())
k = int(input())
start = 1
end = k

while start <= end:
    mid = (start + end) // 2
    tmp = 0

    for i in range(1, N+1):
        tmp += min(mid//i, N)

    if tmp >= k:
        res = mid
        end = mid - 1
    else:
        start = mid + 1

print(res)