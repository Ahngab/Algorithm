from collections import deque

string = input()
N = len(string)
ans = 0
Qa = deque()
Qb = deque()

for i in range(N):
    if string[i] == "A":
        Qa.append(i)
    elif string[i] == "B":
        Qb.append(i)
    elif string[i] == "C" and Qb:
        Qb.popleft()
        ans += 1

while Qa:
    cur = Qa.popleft()
    while Qb and Qb[0] < cur:
        Qb.popleft()

    if Qb:
        Qb.popleft()
        ans += 1

print(ans)