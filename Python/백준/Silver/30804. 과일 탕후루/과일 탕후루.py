N = int(input())
arr = list(map(int, input().split()))

ans = 0
left = 0
cnt = {}
l = 0

for right in range(N):
    if arr[right] in cnt:
        cnt[arr[right]] += 1
    else:
        cnt[arr[right]] = 1
        l += 1
    
    while l > 2:
        cnt[arr[left]] -= 1
        if cnt[arr[left]] == 0:
            del cnt[arr[left]]
            l -= 1
        left += 1

    ans = max(ans, right - left + 1)

print(ans)