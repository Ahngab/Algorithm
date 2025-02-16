import sys

numCnt = [0] * 10

N = list(map(int, list(input())))
for i in N:
    if i == 6 or i == 9:
        if numCnt[6] <= numCnt[9]:
            numCnt[6] += 1
        else:
            numCnt[9] += 1
    else:
        numCnt[i] += 1

print(max(numCnt))
