def solution(citations):
    max_elem = max(citations)
    
    for h in range(max_elem, -1, -1):
        cnt = 0
        for j in range(len(citations)):
            if citations[j] >= h:
                cnt += 1
        if cnt >= h:
                return h
