import sys

input = sys.stdin.readline
E, S, M = map(int, input().split())
e, s, m = 1, 1, 1
cnt = 1

while True:
    if (E - e) % 15 == 0 and (S - s) % 28 == 0 and (M - m) % 19 == 0:
        print(cnt)
        break
    e += 1
    s += 1
    m += 1
    cnt += 1