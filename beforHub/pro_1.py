def solution(denum1, num1, denum2, num2):
    d = denum1 + denum2
    n = num1*denum2+num2

    start = max(d, n)
    gcd = 1

    for x in range(start, 0, -1):
        if d%x==0 and n%x==0:
            gcd = x
    
    anws = [d/x, n/x]
    return anws