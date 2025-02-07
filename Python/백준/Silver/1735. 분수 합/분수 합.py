def findGcd(a, b):
    A = max(a, b)
    B = min(a, b)

    while B != 0:
        A, B = B, A % B
    
    return A


a, b = map(int, input().split())
c, d = map(int, input().split())

gcd = findGcd(b, d)
lcm = int(b*d / gcd)

factor1 = lcm//b
factor2 = lcm//d

a *= factor1
c *= factor2


resultN = a + c
resultD = b * factor1

gcd = findGcd(resultN, resultD)
print(resultN//gcd, resultD//gcd)