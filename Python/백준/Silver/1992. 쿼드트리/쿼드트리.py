import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N = int(input())
arr = [list(map(int, list(input().strip()))) for _ in range(N)]

answer = ""
def tree(n, x, y):
    global answer

    if n == 1:
        answer += str(arr[x][y])
        return
    
    first = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if first != arr[i][j]:
                answer += "("
                tree(n//2, x, y)
                tree(n//2, x, y + n//2)
                tree(n//2, x + n//2, y)
                tree(n//2, x + n//2, y + n//2)
                answer += ")"
                return
    
    answer += str(first)
    return

tree(N, 0, 0)
print(answer)

    
    