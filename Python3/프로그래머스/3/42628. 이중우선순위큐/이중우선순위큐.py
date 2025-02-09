import heapq

def solution(operations):
    answer = []
    heap = []
    
    for op in operations:
        if op[0] == "I":
            heapq.heappush(heap, int(op[2:]))
        
        elif op == "D 1" and heap:
            heap.sort()
            heap.pop()

        elif op == "D -1" and heap:
            heapq.heappop(heap)
    
    if heap:
        heap.sort()
        answer.append(heap[-1])
        answer.append(heap[0])
    else:
        answer.append(0)
        answer.append(0)
        
    return answer