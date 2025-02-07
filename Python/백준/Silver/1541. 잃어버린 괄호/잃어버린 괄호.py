import sys

sum_ = 0
flag = False
form = list(map(int, sys.stdin.readline().strip().replace('-', ' -').replace('+', ' +').split()))

for i in range(len(form)):
    if form[i] < 0:
        flag = True
    if flag:
        sum_ -= abs(form[i])
    else:
        sum_ += form[i]
print(sum_)
