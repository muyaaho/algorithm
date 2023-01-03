def solution(n, times):
    answer = 0
    l = min(times)
    r = max(times)*n
    
    while l<=r:
        m = (l+r)//2
        checked = 0
        
        for time in times:
            checked += m//time
            if checked >= n:
                break
        
        if checked>=n:
            answer = m
            r = m-1
        else:
            l = m+1
    
    return answer