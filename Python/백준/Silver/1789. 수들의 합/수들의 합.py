import sys

N = int(input())
cnt = 1

while True:
    N -= cnt
    if cnt >= N:
        break
    cnt += 1

print(cnt)