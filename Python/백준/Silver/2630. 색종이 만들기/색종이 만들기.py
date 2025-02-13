import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
paper0 = 0
paper1 = 0

def square(n, x, y):
    global paper0, paper1

    if n == 1:
        if arr[x][y] == 0:
            paper0 += 1
        elif arr[x][y] == 1:
            paper1 += 1
        return 

    bit1 = 1
    bit0 = 0
    
    for i in range(n):
        for j in range(n):
            bit1 &= arr[x + i][y + j]
            bit0 |= arr[x + i][y + j]

    if bit1 == 1:
        paper1 += 1
    elif bit0 == 0:
        paper0 += 1
    else:
        square(n//2, x, y)
        square(n//2, x + n//2, y)
        square(n//2, x, y + n//2)
        square(n//2, x + n//2, y + n//2)


square(N, 0, 0)
print(paper0)
print(paper1)
