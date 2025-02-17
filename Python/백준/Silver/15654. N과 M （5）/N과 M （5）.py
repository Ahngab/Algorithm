from itertools import permutations

N, M = map(int, input().split())
arr = list(map(str, sorted(list(map(int, input().strip().split())))))

tmp = []
    
def perm(n, beforeString):
    if n == M:
        print(" ".join(beforeString))
        return
    
    for i in range(N):
        if arr[i] not in beforeString:
            beforeString.append(arr[i])
            perm(n + 1, beforeString)
            beforeString.pop()


perm(0, [])
