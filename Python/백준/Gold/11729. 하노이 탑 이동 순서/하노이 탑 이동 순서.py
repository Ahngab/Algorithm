import sys
sys.setrecursionlimit(10**6)

N = int(input())

def hanoi(n, start, end, assi):
    if n == 1:
        print(start, end)

    else:
        hanoi(n-1, start, assi, end)
        print(start, end)
        hanoi(n-1, assi, end, start)

print(2**N - 1)
hanoi(N, 1, 3, 2)
        