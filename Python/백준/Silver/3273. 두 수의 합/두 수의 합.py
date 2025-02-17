N = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())
cnt = 0
left, right = 0, len(arr) - 1

while left < right:
    sum_ = arr[right] + arr[left]
    if sum_ < x:
        left += 1
    elif sum_ > x :
        right -= 1
    else:
        cnt += 1
        right -= 1
        left += 1

print(cnt)