import sys

end = 2*123456+1
prime = [1] * end
for i in range(end):
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            prime[i] = 0
            break


while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break

    cnt = 0
    for i in range(N+1, 2*N + 1):
        if prime[i] == 1:
            cnt += 1
    print(cnt)