import sys
from collections import deque

N = int(sys.stdin.readline())
data = [tuple(map( int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(len(data)):
    weight = data[i][0]
    height = data[i][1]
    cnt = 1

    for j in range(len(data)):
        if i != j:
            if (data[j][0] > weight and data[j][1] > height):
                cnt += 1
    print(cnt, end=" ")