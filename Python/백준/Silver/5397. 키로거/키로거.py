from collections import deque

def mkString(string):
    q_l = deque()
    q_r = deque()

    for i in string:
        if i == "<":
            if q_l:
                q_r.appendleft(q_l.pop())

        elif i == ">":
            if q_r:
                q_l.append(q_r.popleft())

        elif i == "-":
            if q_l:
                q_l.pop()

        else:
            q_l.append(i)

    return "".join(q_l) + "".join(q_r)

T = int(input())
for _ in range(T):
    print(mkString(input()))
        