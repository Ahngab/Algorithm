import sys

M, N = map(int, sys.stdin.readline().split())
origin = set(sys.stdin.readline().strip() for _ in range(M))
test = list(sys.stdin.readline().strip() for _ in range(N))
cnt = 0


for i in test:
    if i in origin: cnt += 1
print(cnt)