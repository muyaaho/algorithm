def solution(n, t):
    answer = n
    for x in range(t):
        answer *= 2
    return answer