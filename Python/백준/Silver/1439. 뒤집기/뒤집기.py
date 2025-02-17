import sys
sys.setrecursionlimit(10**7)

string = input().strip()
cnt = [0, 0]
flag = string[0]

for i in range(1, len(string)):
    if flag == string[i]:
        continue
    
    else:
        cnt[int(flag)] += 1
        flag = string[i]

cnt[int(flag)] += 1

print(min(cnt))