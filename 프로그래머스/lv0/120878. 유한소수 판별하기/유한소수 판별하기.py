import math

def solution(a, b):
    g = math.gcd(a, b)
    arr = set()
    a //= g
    b //= g
    
    if b == 1:
        return 1
    
    for x in range(2, b+1):
        if b%x == 0:
            while b%x == 0:
                b //= x
            arr.add(x)
            
    if arr == {2,5} or arr == {2} or arr=={5}:
        return 1
    else:
        return 2
