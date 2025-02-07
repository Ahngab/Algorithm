import sys
from collections import deque

def config(string):
    stack = deque()
    for i in string:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                return "NO"
    
    if len(stack) != 0:
        return "NO"
    else:
        return "YES"



T = int(sys.stdin.readline())

for _ in range(T):
    string = sys.stdin.readline().strip()
    print(config(string))
