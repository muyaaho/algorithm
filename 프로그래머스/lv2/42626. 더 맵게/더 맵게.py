from heapq import heapify, heappop, heappush

def solution(scoville, K):
    answer = 0
    
    heapify(scoville)
    while len(scoville)>1:
        if scoville[0] < K:
            heappush(scoville, heappop(scoville)+heappop(scoville)*2)
            answer += 1
        else:
            break
    
    if scoville[0] < K:
        answer = -1
    
    return answer