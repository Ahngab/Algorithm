import sys

N = int(sys.stdin.readline().strip())
arr = list((map(int, sys.stdin.readline().strip().split())))
sortArr = sorted(list(set(arr)))

temp = {sortArr[i]: i for i in range(len(sortArr))}
for i in arr:
    print(temp[i], end=" ")