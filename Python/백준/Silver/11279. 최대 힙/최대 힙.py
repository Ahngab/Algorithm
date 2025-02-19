import heapq, sys

input = sys.stdin.readline
N = int(input())
heap = []

for _ in range(N):
    cmd = int(input())

    if cmd == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, [-cmd, cmd])
