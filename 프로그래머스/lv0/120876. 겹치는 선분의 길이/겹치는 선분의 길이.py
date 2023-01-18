def solution(lines):
    check = [0]*202
    for a, b in lines:
        for i in range(a, b):
            check[i+100] += 1
    
    return len([x for x in check if x>1])