def solution(x):
    a = sum([int(c) for c in str(x)])
    return x%a == 0 