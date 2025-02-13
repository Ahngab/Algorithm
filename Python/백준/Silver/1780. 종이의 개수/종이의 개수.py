import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
paper0, paper1, paper2 = 0, 0, 0

def paper(n, x, y):
    global paper0, paper1, paper2

    if n == 1:
        if arr[x][y] == 0:
            paper0 += 1
        elif arr[x][y] == 1:
            paper1 += 1
        else:
            paper2 += 1
        return 
    
    first = arr[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if first != arr[i][j]:
                paper(n//3, x, y)
                paper(n//3, x + n//3, y)
                paper(n//3, x + n//3*2, y)

                paper(n//3, x, y + n//3)
                paper(n//3, x + n//3, y + n//3)
                paper(n//3, x + n//3*2, y + n//3) 
                
                paper(n//3, x, y + n//3*2)
                paper(n//3, x + n//3, y + n//3*2)
                paper(n//3, x + n//3*2, y + n//3*2)
                return 
    
    if first == 0:
        paper0 += 1
    elif first == 1:
        paper1 += 1
    else:
        paper2 += 1

paper(N, 0, 0)
print(paper2)
print(paper0)
print(paper1)