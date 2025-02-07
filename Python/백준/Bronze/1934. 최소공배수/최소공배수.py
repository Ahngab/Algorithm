def findGcd(a, b):
    A = max(a, b)
    B = min(a, b)

    while B != 0:
        A, B = B, A % B
    
    return A

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    gcd = findGcd(a, b)

    print(int(a * b / gcd))