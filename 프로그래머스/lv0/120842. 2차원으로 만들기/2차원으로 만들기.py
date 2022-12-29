def solution(num_list, n):
    answer = []
    arr= []
    for x in num_list:
        if len(arr) != n:
            arr.append(x)
        if len(arr) == n:
            answer.append(arr)
            arr=[]
    return answer