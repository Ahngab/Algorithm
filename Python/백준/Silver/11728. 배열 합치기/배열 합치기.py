import sys
N, M = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr = [0] * (len(arr1) + len(arr2))


idx1 = 0
idx2 = 0
idx = 0

while idx < len(arr):
    if idx1 == len(arr1):
        while idx2 < len(arr2):
            arr[idx] = arr2[idx2]
            idx += 1
            idx2 += 1
        break

    elif idx2 == len(arr2):
        while idx1 < len(arr1):
            arr[idx] = arr1[idx1]
            idx += 1
            idx1 += 1
        break

    if arr1[idx1] >= arr2[idx2]:
        arr[idx] = arr2[idx2]
        idx2 += 1
        idx += 1
    else:
        arr[idx] = arr1[idx1]
        idx1 += 1
        idx += 1

print(*arr, sep = " ")