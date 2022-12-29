def solution(s):
    answer = ''
    for word in s.split(' '):
        for i, x in enumerate(word):
            if i%2==0:
                answer += x.upper()
            else:
                answer += x.lower()
        answer += ' '
    return answer[:-1]