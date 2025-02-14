import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def pooling(n, x, y):
    if n == 1:
        return arr[x][y]

    piece1 = pooling(n//2, x, y)
    piece2 = pooling(n//2, x + n//2, y)
    piece3 = pooling(n//2, x, y + n//2)
    piece4 = pooling(n//2, x + n//2, y + n//2)
    value = sorted([piece1, piece2, piece3, piece4])[2]
    return value


print(pooling(N, 0, 0))