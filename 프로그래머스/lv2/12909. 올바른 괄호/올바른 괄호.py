from collections import deque

def solution(s):
    answer = True
    
    q = deque()
    for x in s:
        if x == '(':
            q.append(x)
        else:
            try:
                q.pop()
            except:
                return False
    
    if not q:
        return True
    else:
        return False