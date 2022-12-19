def solution(emergency):
    a = {x:i+1 for i, x in enumerate(sorted(emergency, reverse=True))}
    answer = []
    
    #print(a)
    for x in emergency:
        answer.append(a[x])    
    return answer