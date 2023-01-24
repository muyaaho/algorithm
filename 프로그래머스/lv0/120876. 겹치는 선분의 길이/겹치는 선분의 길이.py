# set으로 간단하게 하는 방법 모르겠다

def solution(lines):
    coord = [0]*202
    answer = 0
    
    for to, end in lines:
        for i in range(to, end):
            coord[i] += 1
    
    return len([1 for i in coord if i > 1])