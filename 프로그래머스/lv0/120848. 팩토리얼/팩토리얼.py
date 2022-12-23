def solution(n):
    answer = 1
    mul=1
    for x in range(1, n+2):
        if mul*x > n:
            answer = x
            break
        mul *= x
            
    return answer-1