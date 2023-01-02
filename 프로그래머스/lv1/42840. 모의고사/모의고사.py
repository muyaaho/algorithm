def solution(answers):
    answer = []
    p1 = [1,2,3,4,5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    c = [0, 0, 0]
    
    for i, x in enumerate(answers):
        if p1[i%5] == x:
            c[0] += 1
        if p2[i%8] == x:
            c[1] += 1
        if p3[i%10] == x:
            c[2] += 1
    
    for i, x in enumerate(c, start=1):
        if x == max(c):
            answer.append(i)
    
    return answer