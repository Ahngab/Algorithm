import sys

def khanSet(a, n):
    if n == 1:
        return 
    for i in range(a + n // 3, a + (n // 3) * 2):
        arr[i] = " "
    
    khanSet(a, n // 3)
    khanSet(a + (n // 3) * 2, n // 3)

input = sys.stdin.readline
while True:
    try:
        N = int(input())
        num = 3**N
        arr = ["-"] * num
        khanSet(0, num)
        print("".join(arr))
    except:
        break