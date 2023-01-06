def solution(A,B):
    a = sorted(A)
    b = sorted(B, reverse=True)
    
    return sum([a[i]*b[i] for i in range(len(a))])