N, L = map(int, input().split())
num = sorted(list(map(int, input().split())))

start = num[0]
cnt = 1

for i in num:
    if i in range(start, start + L):
        continue
    else:
        start = i
        cnt += 1
print(cnt)