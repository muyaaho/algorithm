from heapq import heappop, heappush

def solution(operations):
    answer = []
    for x in operations:
        order, num = x.split(' ')
        
        if order == 'I':
            heappush(answer, int(num))
        elif num == '1' and len(answer)>0:
            answer.remove(max(answer))
        elif num == '-1' and len(answer)>0:
            heappop(answer)

    if len(answer)<2:
        return [0,0]
    else:
        return [max(answer), min(answer)]