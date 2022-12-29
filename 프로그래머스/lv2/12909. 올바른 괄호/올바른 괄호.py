from collections import deque

def solution(s):
    deq = deque()
    for x in s:
        if x == '(':
            deq.append(x)
        else:
            if not deq:
                return False
            deq.pop()
    
    if len(deq) == 0: return True
    else: return False
