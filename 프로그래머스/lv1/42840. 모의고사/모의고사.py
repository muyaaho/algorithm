def solution(answers):
    answer = []
    correct = [0,0,0]
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i, x in enumerate(answers):
        if p1[i%5] == x:
            correct[0] += 1
        if p2[i%8] == x:
            correct[1] += 1
        if p3[i%10] == x:
            correct[2] += 1
    
    for i, x in enumerate(correct, start = 1):
        if x == max(correct):
            answer.append(i)
    return answer