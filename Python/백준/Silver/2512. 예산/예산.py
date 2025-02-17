import sys

N = int(input())
moneys = list(map(int, input().split()))
limit = int(input())
min_ = 1
max_ = max(moneys)
res = 0

while min_ <= max_:
    mid = (min_ + max_) // 2
    total = 0
    for money in moneys:
        if money > mid:
            total += mid
        else:
            total += money
    
    if total <= limit:
        res = mid
        min_ = mid + 1
    else:
        max_ = mid - 1

print(res)