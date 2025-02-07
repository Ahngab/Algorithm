import sys

site = {}
N, M = map(int, sys.stdin.readline().strip().split())
for _ in range(N):
    id, pw = sys.stdin.readline().strip().split()
    site[id] = pw

for _ in range(M):
    print(site[sys.stdin.readline().strip()])