def solution(n, k):
    s = n//10 # 0이하면 어차피 0이구나..! 람다 한번 써 본걸로..
    new_k = (lambda x: k-s if k-x>=0 else 0)(s)
    answer = n*12000+new_k*2000
    return answer