def solution(age):
    lage = list(map(int,list(str(age))))
    #print(lage)
    answer = ''
    for x in lage:
        answer += chr(97+x)
    
    return answer
