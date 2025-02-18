from collections import deque

def find(string):
    stack = deque()
    for i in string:
        if stack and stack[-1] == i:
            stack.pop()

        else:
            stack.append(i)

    if stack:
        return False
    else:
        return True
    
T = int(input())
cnt = 0
        
for _ in range(T):
    if find(input()):
        cnt += 1
print(cnt)