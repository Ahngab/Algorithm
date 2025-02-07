import sys

input = sys.stdin.readline
N = int(input())
meeting = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))

maxCnt = 1
endTime = meeting[0][1]

for i in range(1, len(meeting)):
    if meeting[i][0] >= endTime:
        endTime = meeting[i][1]
        maxCnt += 1
print(maxCnt)  