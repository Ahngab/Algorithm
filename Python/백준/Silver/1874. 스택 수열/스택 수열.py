import sys
from collections import deque

N = int(sys.stdin.readline())

num = 1
make = [int(sys.stdin.readline()) for _ in range(N)]
stack = deque([])
made = []
result = []
index = 0


while True:
    if len(made) == N:
        for i in result:
            print(i)
        break

    
    if make[index] < num:
        if stack[-1] != make[index]:
            print("NO")
            break
        else:
            made.append(stack.pop())
            result.append("-")
            index += 1
    
    elif make[index] == num:
        made.append(num)
        num += 1
        index += 1
        result.append("+")
        result.append("-")
    
    else:
        if num != make[index]:
            stack.append(num)
            result.append("+")
            num += 1
        elif num == make[index]:
            made.append(num)
            result.append("+")
            result.append("-")
            num += 1
            index += 1