import sys

input = sys.stdin.readline
N = int(input())

road = list(map(int, input().split()))
nodes = list(map(int, input().split()))
c = nodes[0]
res = 0

for i in range(len(nodes)-1):
    if c > nodes[i]:
        c = nodes[i]
    res += c * road[i]

print(res)