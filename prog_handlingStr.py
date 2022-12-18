def solution(s):
    answer = True
    l = list(s)
    if len(l) == 4 or len(l) == 6:
        for x in l:
            if (ord(x)>=65 and ord(x)<=90) or (ord(x)>=97 and ord(x)<=122):
                answer = False
    else:
        answer = False
    
    return answer