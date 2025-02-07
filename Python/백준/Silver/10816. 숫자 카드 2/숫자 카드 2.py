dict = {}
N = int(input())
cards = input().split()
M = int(input())
comp = input().split()

for i in range(N):
    if cards[i] not in dict:
        dict[ cards[i] ] = 1
    else:
        dict[ cards[i]] += 1
for j in range(M):
    if comp[j] in dict:
        print(dict[comp[j]])
    else:
        print(0)