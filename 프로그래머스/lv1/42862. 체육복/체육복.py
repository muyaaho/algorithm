def solution(n, lost, reserve):

    l = [1]*(n+1)
    
    for x in lost: l[x] -= 1
    for x in reserve: l[x] += 1
    #print(f'set: {l}')
    for i in range(n+1):
        if l[i] == 2 and i > 1 and l[i-1] == 0:
            l[i-1] += 1
            l[i] -= 1
        elif l[i] == 2 and i<n and l[i+1] == 0:
            l[i+1] += 1
            l[i] -= 1
    #print(f'change: {l}')
    answer = len([x for x in l if x != 0])-1
    return answer