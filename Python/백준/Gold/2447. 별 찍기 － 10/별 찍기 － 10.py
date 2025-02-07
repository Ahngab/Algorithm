import sys

def Square(x, y, n):
    if n == 1:
        return
    for i in range(x + (n//3), x + (n//3)*2):
        for j in range(y + (n//3), y + (n//3)*2):
            board[i][j] = ' '
    
    Square(x, y, n//3)
    Square(x + (n//3), y, n//3)
    Square(x + (n//3)*2, y, n//3)

    Square(x, y + (n//3), n//3)
    Square(x + (n//3)*2, y + (n//3), n//3)

    Square(x, y + (n//3)*2, n//3)
    Square(x + (n//3), y + (n//3)*2, n//3)
    Square(x + (n//3)*2, y + (n//3)*2, n//3)

input = sys.stdin.readline
N = int(input())
board = [["*"]*N for _ in range(N)]
Square(0, 0, N)
for i in range(len(board)):
    print("".join(board[i]))