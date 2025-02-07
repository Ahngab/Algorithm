N = int(input())
min_ = 5000


for i in range(N//5+1):
    remain = N - 5*i
    if remain % 3 == 0 and (i + (remain // 3)) < min_:
        min_ = i + (remain // 3)

if min_ == 5000:
    print(-1)
else:
    print(min_)