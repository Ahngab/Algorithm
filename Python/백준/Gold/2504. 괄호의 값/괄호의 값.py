from collections import deque

def check(string):
    stack = deque()
    for i in string:
        if i == "(" or i == "[":
            stack.append(i)
        
        elif i == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                return False
        
        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
            
    if stack:
        return False
    
    return True
        


formula = input().strip()
bracket = set(["(", ")", "[", "]"])

if check(formula):
    stack = deque()

    for i in formula:
        if i == "(" or i == "[":
            if stack and stack[-1] == 1:
                stack.pop()

            stack.append(i)
            stack.append(1)
        
        elif i == "]":
            num = stack.pop()
            stack.pop()
            num *= 3
            stack.append(num)

        elif i == ")":
            num = stack.pop()
            stack.pop()
            num *= 2
            stack.append(num)

        if len(stack) >= 2 and stack[-2] not in bracket and stack[-1] not in bracket:
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num1 + num2)

    print(stack[0])

else:
    print(0)

