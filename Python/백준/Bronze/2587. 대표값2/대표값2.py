import sys 
arr = sorted([int(sys.stdin.readline()) for _ in range(5)])

print(sum(arr) // 5)
print(arr[2])