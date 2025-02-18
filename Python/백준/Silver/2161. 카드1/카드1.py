from collections import deque

queue = deque([i for i in range(1, int(input()) + 1)])

while True:
    print(queue.popleft(), end=" ")

    if not queue:
        break
    queue.append(queue.popleft())