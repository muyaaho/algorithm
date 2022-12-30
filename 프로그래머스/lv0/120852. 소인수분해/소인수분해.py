def solution(n):
    answer = set()
    d=2
    while n>1:
        if n%d==0:
            answer.add(d)
            n//=d
            # print(d)
        else:
            d+=1
    return sorted(answer)