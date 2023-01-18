def solution(babbling):
    can = set(["aya", "ye", "woo", "ma"])
    answer = 0
    
    for word in babbling:
        for c in can:
            if c in word:
                word = word.replace(c, '1'*len(c))
        try:
            if int(word):
                answer += 1
        except:
            pass

    return answer