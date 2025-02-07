N = int(input())
minX = 10001
maxX = -10001
minY = 10001
maxY = -10001


for _ in range(N):
    x, y = map(int, input().split())
    if minX >= x:
        minX = x
    if maxX <= x:
        maxX = x
    if minY >= y:
        minY = y
    if maxY <= y:
        maxY = y
print((maxX - minX) * (maxY - minY))