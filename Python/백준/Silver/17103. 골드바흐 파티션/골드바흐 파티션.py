import sys

end = 1000000+1
prime = [1] * end
prime[0:2] = [0, 0]

for i in range(2, end):
    if prime[i]:
        for j in range(i*2, end, i):
            prime[j] = 0

T = int(sys.stdin.readline())

for _ in range(T):
    cnt = 0
    N = int(sys.stdin.readline())
    for j in range(N//2+1):
        if prime[j] == 1 and prime[N-j] == 1:
            cnt += 1
    print(cnt)