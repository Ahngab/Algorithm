import sys

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
result = [-1]*N
stack = []

for i in range(N):
    while stack and data[stack[-1]] < data[i]:
        result[stack.pop()] = data[i]
    stack.append(i)
print(*result)