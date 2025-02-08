import sys

height = sorted([int(input()) for _ in range(9)])
total = sum(height)
flag = False

for i in range(9):
    for j in range(i,9):
        if total - height[i] - height[j] == 100:
            No1 = i
            No2 = j
            flag = True
            break
    if flag:
        break

for i in range(len(height)):
    if i != No1 and i != No2:
        print(height[i])