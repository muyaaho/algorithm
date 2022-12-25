def solution(my_string):
    answer = []
    for x in my_string:
        print(x)
        if '0'<= x and x<='9':
            answer.append(int(x))
    return sorted(answer)