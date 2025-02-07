import sys

#N 옮길 판, 시작, 어디
def hanoi(N, start, assi, end):
    if N == 1:
        print(start, end)
        return
    hanoi(N-1, start, end, assi)
    print(start, end)
    hanoi(N-1, assi, start, end)

input = sys.stdin.readline
N = int(input())
print(2**N -1)
hanoi(N, 1, 2, 3)
