def solution(n, lost, reserve):
    answer = 0
    people = [1] * (n+1)
    
    for x in lost:
        people[x] -= 1
    
    for x in reserve:
        people[x] += 1
    
    for x in range(n+1):
        if x>1 and people[x] == 2 and people[x-1]==0:
            people[x-1] += 1
            people[x] -= 1
        elif x<n and people[x] == 2 and people[x+1] == 0:
            people[x+1] += 1
            people[x] -= 1
    
    for x in people:
        if x != 0:
            answer += 1
    return answer -1