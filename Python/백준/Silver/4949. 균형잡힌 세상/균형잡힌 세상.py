import sys
from collections import deque

def config(string):
    stack = deque()

    for i in string:
        if i == "[" or i == "(":
            stack.append(i)

        elif i == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                return "no"
        
        elif i == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                return "no"
        
    if len(stack) == 0:
        return "yes"
    
    else:
        return "no"

while True:
    string = sys.stdin.readline().rstrip()
    if string == ".":
        break
    else:
        print(config(string))