def solution(n):
    answer = []
    s = str(n)
    for x in s[::-1]:
        answer.append(int(x))
    return answer