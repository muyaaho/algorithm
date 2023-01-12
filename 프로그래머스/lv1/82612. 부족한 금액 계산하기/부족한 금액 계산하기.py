def solution(price, money, count):
    s = 0
    for x in range(1, count+1):
        s += price*x

    return s-money if s-money>0 else 0