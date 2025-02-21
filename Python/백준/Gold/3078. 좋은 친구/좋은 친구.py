from sys import stdin
from collections import deque
N, K = map(int, stdin.readline().split())
grade = [0] * 21
student = deque()
count = 0
for _ in range(N):
    a = len(stdin.readline().rstrip())
    student.append(a)
    grade[a] += 1
    if len(student) > 0:
        if len(student) > K+1:
            old = student.popleft()
            grade[old]-=1
        count += (grade[a]-1)
print(count)