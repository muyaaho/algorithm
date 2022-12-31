def solution(s):
    answer = ''
    for word in s.split(' '):
        for i, c in enumerate(word):
            if i%2==0:
                answer += c.upper()
            else:
                answer += c.lower()
        answer += ' '
    return answer[:-1]