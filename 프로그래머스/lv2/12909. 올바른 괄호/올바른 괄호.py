from collections import deque

def solution(s):
    answer = True
    q = deque()
    
    for c in s:
        if c=="(":
            q.append(c)
        else:
            if not q:
                return False
            q.pop()
    if not q: return True
    else: return False