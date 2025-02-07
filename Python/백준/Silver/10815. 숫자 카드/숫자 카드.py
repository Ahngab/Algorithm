N = int(input())
arr = set(input().strip().split())

M = int(input())
test = list(input().split())

for i in test:
    if i in arr:
        print("1", end=" ")
    else:
        print("0", end=" ")