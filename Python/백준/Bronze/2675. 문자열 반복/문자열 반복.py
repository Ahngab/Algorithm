def cycle(string, n):
    data = list(string)
    result = "".join([i*n for i in data])
    
    return result

N = int(input())

for i in range(N):
    n, string = input().split()
    print(cycle(string, int(n)))