import math, sys

N = int(sys.stdin.readline())
trees = [int(sys.stdin.readline()) for _ in range(N)]
dist = []


for i in range(len(trees)-1):
     dist.append(trees[i+1] - trees[i])

gcd = math.gcd(*dist)
cnt = 0

for i in dist:
    cnt += (i // gcd)-1
print(cnt)