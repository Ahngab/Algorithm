import sys

input = sys.stdin.readline
S = input().strip()

cnt = []
temp = [0]*26

for i in range(len(S)):
    temp[ord(S[i]) - 97] += 1
    cnt.append(temp[:])
    
q = int(input())

for _ in range(q):
    order = input().split()
    alph = ord(order[0]) - 97
    start, end = map(int, order[1:])
    if start == 0:
        print(cnt[end][alph])
    else:
        print(cnt[end][alph] - cnt[start-1][alph])