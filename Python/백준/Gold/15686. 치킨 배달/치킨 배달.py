from itertools import combinations

def distance(r1, c1, r2, c2):
    return (abs(r1 - r2) + abs(c1 - c2))


N, M = map(int, input().split())
city = []
chicken = []
dist = []

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 1:
            city.append((i, j))
        elif temp[j] == 2:
            chicken.append((i,j))

for comb in combinations(chicken, M):
    t = []
    for c in city:
        d = 100000
        for chick in comb:
            d = min(d, distance(c[0], c[1], chick[0], chick[1]))
        t.append(d)
    dist.append(sum(t))

print(min(dist))


