def solution(routes):
    routes = sorted(routes, key = lambda x: x[1])
    N = len(routes)
    answer = 0
    index = 0
    
    while index < N:
        i = 1
        answer += 1
        while index + i < N and routes[index][1] >= routes[index + i][0]:
            i += 1
        
        index += i 
        
    
    return answer