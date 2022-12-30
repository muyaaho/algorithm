def solution(cipher, code):
    answer = ''
    for i, x in enumerate(cipher, start = 1):
        if i%code == 0:
            answer += x
    return answer