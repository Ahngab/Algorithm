N = int(input())
temp = 1
cnt = 1

while N > temp:
    temp += 6*cnt
    cnt += 1
print(cnt)