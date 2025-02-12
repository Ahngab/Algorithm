import sys
sys.setrecursionlimit(10**6)

def square(n, m):
    global answer

    if n == 0 or m == 0:
        return 
    
    else:
        answer += 1
        if m > n:
            square(n, m-n)
        else:
            square(n-m, m)

input = sys.stdin.readline
N, M = map(int, input().split())
answer = 0
square(N, M)
print(answer)