import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
string = input().strip()

cursor, cnt, result = 0, 0, 0

while cursor < M - 1:
    if string[cursor:cursor + 3] == "IOI":
        cnt += 1
        cursor += 2
        if cnt == N:
            result += 1
            cnt -= 1
    
    else:
        cursor += 1
        cnt = 0

print(result)