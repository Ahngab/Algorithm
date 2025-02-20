thirty1 = {1, 3, 5, 7, 8, 10, 12}
thirty = {4, 6, 9, 11}
day = {1: "MON", 2: "TUE", 3: "WED", 4: "THU", 
5: "FRI", 6: "SAT", 0: "SUN"}

M, D = map(int, input().split())
date = D

for i in range(1, M):
    if i in thirty:
        date += 30
    elif i in thirty1:
        date += 31
    else:
        date += 28

print(day[date % 7])