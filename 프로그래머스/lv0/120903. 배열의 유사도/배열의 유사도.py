def solution(s1, s2):
    answer = [1 for x in s1 if x in s2]
    return len(answer)