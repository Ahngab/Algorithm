N, S = map(int, input().split())
arr = list(map(int, input().split()))

right, left = 0, 0
sum_ = 0
cnt = 1000000

while True:
    if sum_ >= S:
        cnt = min(cnt, right - left)
        sum_ -= arr[left]
        left += 1

    elif right == N:
        break

    else:
        sum_ += arr[right]
        right += 1
    


if cnt == 1000000:
    print(0)

else:
    print(cnt)   