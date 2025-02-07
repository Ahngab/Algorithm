N = 1
for i in range(3):
    N *= int(input())

number = str(N)

for i in range(10):
    print(number.count(str(i)))