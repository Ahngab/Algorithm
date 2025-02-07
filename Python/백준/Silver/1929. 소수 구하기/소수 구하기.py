import sys

M, N = map(int, sys.stdin.readline().split())

for i in range(M, N+1):
    flag = True
    if i == 1:
        flag = False
    else:
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                flag = False
                break
    if flag:
        print(i)