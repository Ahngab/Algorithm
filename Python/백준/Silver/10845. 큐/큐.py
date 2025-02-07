import sys

def push(X):
    global queue
    queue.insert(0, X)

def pop():
    global queue
    print(queue.pop()) if len(queue) > 0 else print(-1)

def size():
    global queue
    print(len(queue))

def empty():
    global queue
    print(1) if len(queue) == 0 else print(0)

def front():
    global queue
    print(queue[-1]) if len(queue) > 0 else print(-1)

def back():
    global queue
    print(queue[0]) if len(queue) > 0 else print(-1)

N = int(sys.stdin.readline())
queue = []
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
    elif command[0] == "front":
        front()
    else:
        back()