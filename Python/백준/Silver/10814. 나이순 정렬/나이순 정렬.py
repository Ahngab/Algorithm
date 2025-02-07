import sys
N = int(sys.stdin.readline())
data = []
for i in range(N):
    age, name = sys.stdin.readline().rstrip().split()
    data.append([int(age), name])
for i in sorted(data, key=lambda x: x[0]):
    print(*i)