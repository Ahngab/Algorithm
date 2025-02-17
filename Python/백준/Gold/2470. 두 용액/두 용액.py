N = int(input())
solution = sorted(list(map(int, input().split())))

index = len(solution)
for i in range(len(solution)):
    if solution[i] > 0:
        index = i
        break

acid = solution[:index]
base = solution[index:]
min_ = 2000000001
res1 = -1000000000
res2 = -1000000000

if len(acid) >= 2:
    if abs(min_) > abs(acid[-1] + acid[-2]):
        min_ = acid[-1] + acid[-2]
        res1 = acid[-1]
        res2 = acid[-2]

if len(base) >= 2:
    if abs(min_) > abs(base[0] + base[1]):
        min_ = base[0] + base[1]
        res1 = base[1]
        res2 = base[0]

if len(acid) >= 1 and len(base) >= 1:
    for i in range(len(acid)):
        start = 0
        end = len(base) - 1
        flag = False

        while start <= end:
            mid  = (start + end) // 2
            made = acid[i] + base[mid]

            if  made > 0:
                end = mid - 1

            elif made < 0:
                start = mid + 1

            else:
                min_ = made
                res1 = acid[i]
                res2 = base[mid]
                flag = True
                break

            if abs(min_) > abs(made):
                min_ = made
                res1 = acid[i]
                res2 = base[mid]

        if flag: break

print(*sorted([res1, res2]), sep = " ")