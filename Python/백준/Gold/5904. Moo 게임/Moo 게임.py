import sys

s0 = ["m", "o", "o"]
N = int(input())

def Moo(n, k, l):
    if n <= 3:
        print(s0[n-1])
        return
    
    new_l = 2 * l + k + 3
    if new_l < n:
        Moo(n, k + 1, new_l)
    
    else:
        if l < n <= l + k + 3:
            if n == l + 1:
                print('m')
            else:
                print('o')
        else:
            Moo(n - (l + k + 3), 1, 3)
    

Moo(N, 1, 3)