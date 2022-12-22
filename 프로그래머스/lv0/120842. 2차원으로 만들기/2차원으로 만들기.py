def solution(num_list, n):
    answer = []
    l = []
    for i,x in enumerate(num_list):
        if i%n == n-1:
            l.append(x)
            answer.append(l)
            l=[]
        else:
            l.append(x)
            
    return answer