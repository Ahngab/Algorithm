def find(m, n, x, y):
    k = x
    while k <= m * n:
        if (k-x) % m == 0 and (k-y) % n == 0:
            return k
        k += m
    return -1



T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    
    print(find(M, N, x, y))

 