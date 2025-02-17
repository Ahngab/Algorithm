N, M  = map(int, input().split())
trees = list(map(int, input().split()))
total = sum(trees)
num = len(trees)

min_ = 0
max_ = max(trees)
res = 0

while min_ <= max_:
    mid = (min_ + max_) // 2
    cut = 0
    for tree in trees:
        if mid < tree:
            cut += tree - mid

    if cut >=M:
        res = mid
        min_ = mid + 1
    else:
        max_ = mid - 1
print(res)