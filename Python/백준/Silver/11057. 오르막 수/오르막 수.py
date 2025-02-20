import math
n = int(input())
print(math.comb(10 + n - 1, n) % 10007)