def solution(my_string):
    answer = 0
    tosum = []
    for x in my_string:
        if '0'<=x and x<='9':
            tosum.append(int(x))
    return sum(tosum)