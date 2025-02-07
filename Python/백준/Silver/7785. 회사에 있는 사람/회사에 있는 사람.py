import sys

N = int(sys.stdin.readline())
worker = {}

for _ in range(N):
    name, info = sys.stdin.readline().strip().split()
    if info == "leave":
        del worker[name]
    elif info == "enter":
        worker[name] = info

for i in sorted(worker, reverse=True):
    print(i)