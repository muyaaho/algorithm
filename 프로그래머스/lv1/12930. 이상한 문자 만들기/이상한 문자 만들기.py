def solution(s):
    answer = ''
    slist = s.split(' ')
    for word in slist:
        for i, x in enumerate(word):
            if i%2==0:
                answer += x.upper()
            else:
                answer += x.lower()
        answer += ' '
    return answer[:-1]