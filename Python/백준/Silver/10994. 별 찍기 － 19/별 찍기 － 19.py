import sys
sys.setrecursionlimit(10**6)

N = int(input())
limit = 1 + ((N-1) * 4)
arr = [[" "]*(limit) for _ in range(limit)]

def star(n, x, y):
    if n == 0:
        arr[x][y] = "*"
        return

    else:
        x_end = x + (n * 4)
        y_end = y + (n * 4)
        for i in range(x, x_end+1):
            arr[i][y] = "*"
            arr[i][y_end] = "*"

        for i in range(y, y_end+1):
            arr[x][i] = "*"
            arr[x_end][i] = "*"


        return star(n - 1, x + 2, y + 2)

star(N-1, 0, 0)
for i in arr:
    print("".join(i))