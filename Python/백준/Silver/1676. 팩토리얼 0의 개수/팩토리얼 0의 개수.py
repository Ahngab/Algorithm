import math

N = str(math.factorial(int(input())))
cnt = 0
for i in N[::-1]:
    if i == "0":
        cnt += 1
    else:
        break
print(cnt)