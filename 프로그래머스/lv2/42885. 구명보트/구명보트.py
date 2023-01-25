from collections import deque

def solution(people, limit):
    people.sort()
    answer = 0
    p = deque(people)
    
    while p:
        if len(p)>1:
            if p[0] + p[-1] <= limit:
                p.popleft()
                p.pop()
                answer += 1
            else:
                p.pop()
                answer += 1
        else:
            answer += 1        
            break
    
    return answer