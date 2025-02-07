N, M = map(int, input().split())
cards = list(map(int, input().split()))
target = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            temp = cards[i] + cards[j] + cards[k]
            if target <= temp and temp <= M:
                target = temp
print(target)