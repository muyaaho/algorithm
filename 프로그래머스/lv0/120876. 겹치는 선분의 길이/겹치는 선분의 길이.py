def solution(lines):
    arr = [0]*202
    
    for start, end in lines:
        for i in range(start, end):
            arr[i] += 1
    
    return len([1 for x in arr if x > 1])