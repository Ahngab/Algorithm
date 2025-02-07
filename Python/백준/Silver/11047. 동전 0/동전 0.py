import sys

N, K = map(int, sys.stdin.readline().split())

coins = sorted([int(sys.stdin.readline()) for _ in range(N)], reverse=True)
result = 0

for index in range(len(coins)):
    if K < coins[index]:
        pass
    else:
        Q = K // coins[index]
        K -= Q * coins[index]
        result += Q
print(result)
