from heapq import heappop, heappush

def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    heap = []
    
    while i<len(jobs):
        for req, time in jobs:
            if start< req <= now:
                heappush(heap, [time, req])
        
        if heap:
            time, req = heappop(heap)
            start = now
            now += time
            answer += now - req
            i+=1
        else:
            now += 1
    
    return answer//len(jobs)