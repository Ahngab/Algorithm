import sys
N = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for i in range(N)]
for i in sorted(data):
    print(i)