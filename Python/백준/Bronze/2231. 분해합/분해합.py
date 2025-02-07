N = int(input())

for i in range(N+1):
    sum_ = sum(list(map(int, str(i))))
    sum_ += i
    if sum_ == N:
        print(i)
        break
    if i == N:
        print(0)