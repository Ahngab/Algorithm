import sys

input = sys.stdin.readline
met = {"ChongChong"}
N = int(input())

for _ in range(N):
    men = input().strip().split()
    if men[0] in met:
        met.add(men[1])

    elif men[1] in met:
        met.add(men[0])

print(len(met))