from collections import deque

def solution(people, limit):
    cnt = 0
    people = deque(sorted(people, reverse = True))
    
    while people:
        L = limit
        cnt += 1
        L -= people.popleft()
        
        if people and L - people[-1] >= 0:
            people.pop()

    return cnt