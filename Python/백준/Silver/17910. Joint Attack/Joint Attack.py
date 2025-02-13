import sys
sys.setrecursionlimit(10**6)

def fraction(deno, nue):
    global index

    if index == 0:
        return deno, nue
    
    else:
        index -= 1
        return fraction(X[index] * deno + nue, deno)

N = int(input())
X = list(map(int, input().split()))
index = len(X)
deno, nue = fraction(1, 0)
print(str(deno) + "/" + str(nue))