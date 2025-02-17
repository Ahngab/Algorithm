N, M = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
right, left = 0, 0
sum_ = 0

while right < N:
    sum_ += A[right]

    while sum_ > M:
        sum_ -= A[left]
        left += 1

    if sum_ == M:
        cnt += 1
    
    right += 1

print(cnt)