def solution(targets):
    targets = sorted(targets, key = lambda x: (x[1], x[0]))
    answer = 1
    
    e = targets[0][1]
    for target in targets:
        if target[0] >= e:
            answer += 1
            e = target[1]
    return answer