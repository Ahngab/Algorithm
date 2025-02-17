from itertools import permutations

N, M = map(int, input().split())
arr = list(map(str, sorted(list(map(int, input().strip().split())))))

for i in permutations(arr, M):
    print(" ".join(i))