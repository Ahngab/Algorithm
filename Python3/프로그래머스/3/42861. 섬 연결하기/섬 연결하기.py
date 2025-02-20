def solution(n, costs):
    costs = sorted(costs, key = lambda x: x[2])
    print(costs)
    already = set([costs[0][0]])
    answer = 0
    
    while len(already) != n:
        for i in costs:
            u, v, c = map(int, i)

            if u in already and v in already:
                continue

            if u in already:
                already.add(v)
                answer += c
                break

            if v in already:
                already.add(u)
                answer += c
                break
            

            
    return answer
        
            