from collections import deque

N = int(input())
arr = list(map(int, input().split()))[::-1]

stack = deque()
res = [0]*(N)

for i in range(N):
    if stack:
        if arr[i] < stack[-1][1]:
            stack.append([i, arr[i]])

        else:
            while stack and stack[-1][1] < arr[i]:
                idx, val = stack.pop()
                res[N - idx - 1] = N - i

            stack.append([i, arr[i]])

    else:
        stack.append([i, arr[i]])

print(*res, sep=" ")