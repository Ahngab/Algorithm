N = int(input())
crd = []
for i in range(N):
    crd.append(list(map(int,input().split())))
for i in sorted(crd):
    print(i[0],end=' ')
    print(i[1])