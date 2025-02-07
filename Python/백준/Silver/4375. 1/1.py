import sys

input = sys.stdin.readline
while True:
    try:
        N = int(input())
        num = 1
        digit = 1
        while num % N != 0:
            num *= 10
            num += 1
            digit += 1
        print(digit)
    except:
        break