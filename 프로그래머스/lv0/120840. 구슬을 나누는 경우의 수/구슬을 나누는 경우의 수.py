def solution(balls, share):
    
    bunja, bunmo = 1,1
    for x in range(1, balls+1):
        bunja *= x
    for x in range(1, (balls-share)+1):
        bunmo *= x
    for x in range(1, share+1):
        bunmo *= x
    answer = bunja/bunmo
    return answer