import sys

N = int(sys.stdin.readline())
arr = set(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline())
compare = list(map(int, sys.stdin.readline().rstrip().split()))

for i in compare:
    print(1) if i in arr else print(0)