import sys

N = int(sys.stdin.readline())
times = list(sorted(list(map(int, sys.stdin.readline().split()))))
num = 0

for i in times:
    num += i*N
    N -= 1
print(num)