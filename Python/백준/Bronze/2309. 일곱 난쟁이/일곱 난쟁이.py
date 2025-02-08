import sys

input = sys.stdin.readline
height = sorted([int(input()) for _ in range(9)])
total = sum(height)

for i in range(9):
    for j in range(i+1,9):
        if total - height[i] - height[j] == 100:
            for k in range(len(height)):
                if k != i and k != j:
                    print(height[k])
            exit()