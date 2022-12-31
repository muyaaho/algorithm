def solution(my_string, num1, num2):
    answer = ''
    a = my_string[num1]
    b = my_string[num2]
    for i, c in enumerate(my_string):
        if i==num1:
            answer += b
        elif i == num2:
            answer += a
        else:
            answer += c
    return answer