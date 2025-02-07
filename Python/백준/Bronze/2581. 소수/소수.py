def configPrime(n):
    flag = 1

    if n == 1:
        return 0
    
    if n == 2:
        return 1

    for i in range(2, int(n**0.5)+2):
        if n % i == 0:
            flag = 0
            break

    return flag

M = int(input())
N = int(input())
firstFlag = 1
sum_ = 0
min_ = -1

for i in range(M, N+1):
    if i == 1:
        continue
    else:
        if configPrime(i):
            if firstFlag:
                min_ = i
                firstFlag = 0
            sum_ += i

if min_ == -1:
    print(-1)

else:
    print(sum_)
    print(min_)