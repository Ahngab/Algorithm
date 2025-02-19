T = int(input())

for _ in range(T):
    N = int(input())
    dict = {}

    for _ in range(N):
        name, category = map(str, input().split())
        if category in dict:
            dict[category] += 1
        else:
            dict[category] = 1
    
    res = 1
    for i in dict.values():
        res *= (i+1)
    print(res-1)