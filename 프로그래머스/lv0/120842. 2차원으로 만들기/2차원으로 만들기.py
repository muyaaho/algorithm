def solution(num_list, n):
    answer = []
    addd = []
    for i, x in enumerate(num_list, start = 1):
        if i%n == 0:
            addd.append(x)
            answer.append(addd)
            addd=[]
        else:
            addd.append(x)
    return answer