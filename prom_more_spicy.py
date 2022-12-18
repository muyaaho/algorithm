# 시간이 오래 걸리는 방법 for: O(n), sort(): O(nlogn)
# def solution(scoville, K):
#     answer = 0
#     count = 0
#     for x in scoville:
#         if scoville[0] < K:
#             if len(scoville)==1:
#                 return -1
#             else:
#                 count += 1
#                 mix_food = scoville[0] + scoville[1]
#                 scoville.pop(0) #필기[],()
#                 scoville.pop(1)
#                 scoville.append(mix_food)
#                 scoville.sort()
#     answer = count
    
#     return answer

import heapq

def solution(scoville, K):
    heap=[]
    count = 0
    
    for x in scoville:
        heapq.heappush(heap, x)
    
    print('heap', heap)
    while len(heap) > 1:
        if heap[0] < K:
            heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap)*2)
            print('while문의 heap',heap)
            count += 1
        else:
            break
    if heap[0] < K:
        answer = -1
    else:
        answer = count
        
    return answer

print(solution([1,2,3,9,10,12], 7))