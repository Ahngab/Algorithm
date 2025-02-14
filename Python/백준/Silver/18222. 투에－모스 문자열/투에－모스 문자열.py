import sys
sys.setrecursionlimit(10**6)
k = int(input())

def num(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    elif n  % 2 == 0:
        return num(n//2)
    
    else:
        return 1 - num(n//2)

print(num(k-1))