import sys

input = sys.stdin.readline
numCnt = [0] * 9
N = list(map(int, list(input().strip())))

for i in N:
    if i == 9:
        numCnt[6] += 1
    else:
        numCnt[i] += 1

if numCnt[6] % 2 == 0:
    numCnt[6] //= 2
else:
    numCnt[6] = int(numCnt[6]/2) + 1
print(max(numCnt))