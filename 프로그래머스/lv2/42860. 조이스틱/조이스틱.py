def solution(name):
    answer = 0
    minm = len(name)-1
    # 전체 만들 수 있는 수
    for x in name:
        answer += min(abs(ord('A')-ord(x)), 26-abs(ord('A')-ord(x)))
    
    # A가 연속으로 나올 때
    for i, c in enumerate(name):
        next = i+1
        while next < len(name) and name[next] == 'A':
            next += 1
        minm = min(minm, 2*i + len(name) - next, i+2*(len(name)-next))
        
    return answer+minm