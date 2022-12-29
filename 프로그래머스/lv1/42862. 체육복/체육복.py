def solution(n, lost, reserve):
    p = [1]*(n+1)
    
    for x in lost: p[x] -= 1
    for x in reserve: p[x] += 1
    
    for i in range(n+1):
        if i>1 and p[i] == 2 and p[i-1] == 0:
            p[i] -= 1
            p[i-1] += 1
        elif i<n and p[i] == 2 and p[i+1] == 0:
            p[i] -= 1
            p[i+1] += 1
            
    return n-len([x for x in p if x == 0])