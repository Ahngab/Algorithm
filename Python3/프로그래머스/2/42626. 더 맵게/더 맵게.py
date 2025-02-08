import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    
    while len(scoville) >= 2:
        if scoville[0] >= K:
            return answer
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min1 + min2*2)
        answer += 1
        
    if scoville[0] < K:
        return -1
    else:
        return answer