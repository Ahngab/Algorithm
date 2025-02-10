from itertools import permutations

def solution(numbers):
    answer = 0
    #Permutations
    arr = list(numbers)
    possible = set()
    for i in range(1, len(arr)+1):
        temp = [''.join(j) for j in list(permutations(arr, i))]
        for j in temp:
            possible.add(int(j))
    
    #Prime number
    limit = max(possible)
    prime = [1] * (limit + 1)
    for i in range(2, limit + 1):
        if prime[i]:
            for j in range(i+i, limit + 1, i):
                prime[j] = 0
            
    prime[0], prime[1] = 0, 0
    
    for i in possible:
        if prime[i] == 1:
            answer += 1

    return answer