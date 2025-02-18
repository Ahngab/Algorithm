from collections import deque

formula = input().strip()
stack = deque()
ans = []

for i in range(len(formula)):
    if formula[i] == "(":
        stack.append("(")

    elif formula[i] == ")":
        while stack and stack[-1] != "(":
            ans.append(stack.pop())
        stack.pop()

    elif formula[i] == "*" or formula[i] == "/":
        while stack and (stack[-1] == "*" or stack[-1] == "/"):
            ans.append(stack.pop())
        stack.append(formula[i])

    elif formula[i] == "+" or formula[i] == "-":
        while stack and stack[-1] != "(":
            ans.append(stack.pop())
        stack.append(formula[i])
    else:
        ans.append(formula[i])

while stack:
    ans.append(stack.pop())
print(*ans, sep="")