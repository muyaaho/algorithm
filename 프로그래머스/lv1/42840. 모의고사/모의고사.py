def solution(answers):
    answer = []
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0,0,0]
    
    
    for i, score in enumerate(answers):
        if p1[i%5] == score:
            count[0] += 1
        if p2[i%8] == score:
            count[1] += 1
        if p3[i%10] == score:
            count[2] += 1
    
    for i in range(3):
        if count[i] == max(count):
            answer.append(i+1)
    return answer