def solution(N, number):
    answer = 0
    s = [set() for _ in range(8)]
    for i, x in enumerate(s, start = 1):
        x.add(int(str(N)*i))
        
    for i in range(8):
        for j in range(i):
            for o1 in s[j]:
                for o2 in s[i-j-1]:
                    s[i].add(o1+o2)
                    s[i].add(o1-o2)
                    s[i].add(o1*o2)
                    if o2 != 0:
                        s[i].add(o1//o2)
        if number in s[i]:
            answer = i+1
            break
        else:
            answer = -1
    
    return answer