def solution(s):
    return ''.join([x for x in sorted(s) if s.count(x)==1])