import sys

N, M = map(int, sys.stdin.readline().split())
dic = dict()
num = 1

for _ in range(N):
    poketmon = sys.stdin.readline().rstrip()
    if poketmon not in dic:
        dic[poketmon] = num
        dic[str(num)] = poketmon
        num += 1

for _ in range(M):
    Q = sys.stdin.readline().strip()
    print(dic[Q])