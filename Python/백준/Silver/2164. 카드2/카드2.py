import sys
N = int(sys.stdin.readline())

if N == 1 or N == 2:
    print(N)
else:
    two = 1
    while two < N:
        two *= 2
    print( int((N - two/2)) * 2)