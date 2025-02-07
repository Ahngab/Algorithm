import sys

T = int(sys.stdin.readline())
for i in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    people = [[0]*n for _ in range(k+1)]
    
    for i in range(n):
        people[0][i] = i+1
        
    for i in range(1,k+1):
        for j in range(n):
            people[i][j] = sum(people[i-1][:j+1])
            
    print(people[k][n-1])