from itertools import permutations

def solution(numbers):
    #Prime
    limit = 1000000
    prime = [1] * (limit + 1)
    for i in range(2, limit + 1):
        for j in range(2, limit//i+1):
            prime[i*j] = 0
    
    prime[0] = 0
    prime[1] = 0
    
    #Permutation
    answer = 0
    result = set()

    for i in range(1, len(numbers)+1):
        temp = list(permutations(numbers, i))
        for j in range(len(temp)):
            result.add(int(''.join(temp[j])))
    
    for i in result:
        if prime[i] == 1:
            answer += 1

    return answer