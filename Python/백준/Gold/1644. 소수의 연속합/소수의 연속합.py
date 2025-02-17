N = int(input())
prime = [1] * (N+1)
prime[0:2] = [0, 0]
for i in range(2, N + 1):
    for j in range(i+i, N + 1, i):
        prime[j] = 0

p = []
for i in range(1, N + 1):
    if prime[i] == 1:
        p.append(i)

left, right = 0, 0
sum_ = 0
cnt = 0

while right < len(p):
    sum_ += p[right]
    right += 1

    while sum_ > N:
        sum_ -= p[left]
        left += 1
    
    if sum_ == N:
        cnt += 1

print(cnt)