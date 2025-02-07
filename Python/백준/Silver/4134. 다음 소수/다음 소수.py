import sys

def configPrime(n):
    if n == 0 or n == 1:
        return 0

    elif n == 2:
        return 1

    for i in range(2, int(n**0.5) + 2):
        if n % i == 0:
            return 0
    return 1

N = int(sys.stdin.readline())

for _ in range(N):
    n = int(sys.stdin.readline())
    num = n

    while True:
        if configPrime(num):
            print(num)
            break
        num += 1