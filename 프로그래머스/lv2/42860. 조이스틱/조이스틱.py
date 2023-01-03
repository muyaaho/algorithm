def solution(name):
    answer = sum(min(abs(ord('A') - ord(n)), 26-abs(ord('A')-ord(n))) for n in name )
    mm = len(name)-1
    
    for i, c in enumerate(name):
        nxt = i+1
        while nxt < len(name) and name[nxt] == 'A':
            nxt += 1
        mm = min(mm, 2*i+len(name)-nxt, i+ 2*(len(name)-nxt))
    return answer+mm