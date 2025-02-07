import sys

input = sys.stdin.readline
names = set()
cnt = 0

N = int(input())

for _ in range(N):
    string = input().strip()
    if string == "ENTER":
        names.clear()
        continue
    
    elif (string not in names):
        cnt += 1
        names.add(string)

print(cnt)