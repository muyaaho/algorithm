def solution(s):
    answer = ''
    return ''.join(sorted([ch for ch in s if s.count(ch) == 1]))