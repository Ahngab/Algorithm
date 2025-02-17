import sys, bisect
input = sys.stdin.readline

N = int(input())
A = [*map(int, input().split())]

LIS = [A[0]]


for item in A:
    if LIS[-1] < item:
        LIS.append(item)
    else:
        idx = bisect.bisect_left(LIS, item)
        LIS[idx] = item

print(len(LIS))

