x = []
y = []

for _ in range(3):
    x1, y1 = map(int, input().split())
    x.append(x1)
    y.append(y1)

for i in x:
    if x.count(i) == 1:
        targetX = i
for i in y:
    if y.count(i) == 1:
        targetY = i
print(targetX, targetY)