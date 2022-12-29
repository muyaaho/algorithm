def solution(n, lost, reserve):
    arr = [1]*(n+1)
    
    for x in lost:
        arr[x] -= 1
    for x in reserve:
        arr[x] += 1
    
    for x in range(n+1):
        if x > 1 and arr[x] == 2 and arr[x-1] == 0:
            arr[x-1] += 1
            arr[x] -= 1
        elif x < n and arr[x] == 2 and arr[x+1] == 0:
            arr[x+1] += 1
            arr[x] -= 1
    
    answer = [x for x in arr if x != 0]
    return len(answer)-1