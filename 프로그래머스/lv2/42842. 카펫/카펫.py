def solution(brown, yellow):
    x, y = 0, 0
    
    answer = []
    
    for i in range(1, yellow+1):
        if yellow%i == 0:
            x = yellow//i
            y = i
            if 2*(x+y)+4 == brown:
                answer.append(x+2)
                answer.append(y+2)
                break
    return answer