flag = [0] * 42
num = [int(input()) % 42 for _ in range(10)]
for i in range(10):
    flag[num[i]] = 1
print(flag.count(1))