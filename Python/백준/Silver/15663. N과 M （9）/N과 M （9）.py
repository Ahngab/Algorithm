from itertools import permutations

N, M = map(int, input().split())
arr = list(map(str, sorted(list(map(int, input().strip().split())))))
arr = permutations(arr, M)
answer = []

for i in set(arr):
    answer.append(list(map(int, i)))

for i in sorted(answer):
    print(*i)