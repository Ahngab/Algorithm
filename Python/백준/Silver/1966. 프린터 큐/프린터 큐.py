import sys
from collections import deque

T = int(input())

for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    
    queue = deque(list(map( int, sys.stdin.readline().split() )))
    cnt = 0

    while queue:
        max_num = max(queue)
        front = queue.popleft()
        M -= 1

        if max_num == front:
            cnt += 1
            if M < 0:
                print(cnt)
                break
        
        else:
            queue.append(front)
            if M < 0:
                M = len(queue) - 1