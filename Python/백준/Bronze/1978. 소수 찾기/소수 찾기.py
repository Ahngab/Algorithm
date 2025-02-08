import sys

limit = 1000
prime = [0] * (limit + 1)
prime[0:2] = [1,1]

for i in range(2, limit + 1):
    for j in range(2, limit//i + 1):
        prime[i*j] = 1

input = sys.stdin.readline
N = int(input())
cnt = 0
test = list(map(int, input().split()))
for i in test:
    if prime[i] == 0:
        cnt += 1
print(cnt)