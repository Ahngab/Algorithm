import sys
sys.setrecursionlimit(10**6)

def chair(n, row, col):
    
    if n == 1:
        return chairs[row][col]
    
    else:
        temp = []
        temp.append(chair(n//2, row, col))
        temp.append(chair(n//2, row, col + n//2))
        temp.append(chair(n//2, row + n//2, col))
        temp.append(chair(n//2, row + n//2, col + n//2))
        return sorted(temp)[1]

input = sys.stdin.readline
N = int(input())
chairs = [list(map(int, input().split())) for _ in range(N)]
print(chair(N, 0, 0))