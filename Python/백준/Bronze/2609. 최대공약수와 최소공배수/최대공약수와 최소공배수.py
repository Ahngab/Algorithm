import math, sys

input = sys.stdin.readline
A, B = map(int, input().split())
gcd = math.gcd(A, B)
print(gcd)
print((A*B)//gcd)