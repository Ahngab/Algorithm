string = input().strip()
bomb = input().strip()

bombLength = len(bomb)
stringLength = len(string)
stack = []

for i in range(len(string)):
    stack.append(string[i])

    if len(stack) >= bombLength and "".join(stack[-bombLength:]) == bomb:
        for _ in range(bombLength):
            stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")