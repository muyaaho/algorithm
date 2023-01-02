def solution(quiz):
    answer = []
    
    for x in quiz:
        s = x.split(" ")
        if eval("".join(s[:3])) == int(s[-1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer