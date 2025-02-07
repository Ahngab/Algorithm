import sys

def push(X):
    global stack
    stack.append(X)

def pop():
    global stack
    print(stack.pop()) if len(stack) > 0 else print(-1)

def size():
    global stack
    print(len(stack))

def empty():
    global stack
    print(1) if len(stack) == 0 else print(0)

def top():
    global stack
    print(stack[-1]) if len(stack) > 0 else print(-1)

N = int(sys.stdin.readline())
stack = []
for i in range(N):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == "push":
        push(command[1])
    elif command[0] == "pop":
        pop()
    elif command[0] == "size":
        size()
    elif command[0] == "empty":
        empty()
    else:
        top()