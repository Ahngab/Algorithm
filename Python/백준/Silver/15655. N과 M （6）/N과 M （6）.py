import sys

input = sys.stdin.readline
N, M = map(int, input().strip().split())
arr = sorted(list(map(int, input().split())))


def perm(n, beforeString, beforeArr):
    if n == M:
        print(" ".join(map(str, beforeArr)))
        return

    else:
        for i in range(N):
            if beforeString < arr[i]:
                beforeArr.append(arr[i])
                perm(n + 1, arr[i], beforeArr)
                beforeArr.pop()

perm(0, -1, [])
