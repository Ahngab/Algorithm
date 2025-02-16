import sys

input = sys.stdin.readline
N = int(input())
interview = []
for i in range(1, N + 1):
    t, p = map(int, input().split())
    interview.append([i, t + i, p])     #시작, 끝나는 날, 돈

max_ = 0

def inter(beforeEndDay, money):
    global max_
    
    max_ = max(max_, money)  
    for i in range(len(interview)):
        if beforeEndDay <= interview[i][0] and interview[i][1] <= N+1:
            inter(interview[i][1], money + interview[i][2])
 

inter(1, 0)
print(max_)