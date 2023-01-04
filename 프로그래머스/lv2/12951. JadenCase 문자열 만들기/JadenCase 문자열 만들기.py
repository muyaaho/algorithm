def solution(s):
    l = s.lower().split(' ')
    answer = ''
    for word in l:
        try:
            word = word.replace(word[0], word[0].upper(), 1)
            answer += word+' '
        except:
            answer += ' '
    return answer[:-1]