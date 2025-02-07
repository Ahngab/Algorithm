import sys
N = int(sys.stdin.readline())
flag = True
data = list(map(int, sys.stdin.readline().rstrip().split()))
result = []

for i in data:
    if i > 2:
        for j in range(2, i):
            if i % j == 0:
                flag = False
        if flag:
            result.append(i)
        else:
            flag = True
    elif i == 2:
        result.append(i)
print(len(result))