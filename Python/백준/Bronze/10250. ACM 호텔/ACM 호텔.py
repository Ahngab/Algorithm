def room(H, W, person):
    if person % H == 0:
        floor = H
    else:
        floor = person % H
    
    if (person // H) == W:
        right = W
    elif floor == H:
        right = person // H
    else:
        right = (person // H) + 1
    
    if right <= 9:
        right = "0" + str(right)
    
    return str(floor) + str(right)

N = int(input())

for i in range(N):
    H, W, person = map(int, input().split())
    print(room(H, W, person))