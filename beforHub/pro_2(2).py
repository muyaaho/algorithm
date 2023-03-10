#최빈값 구하기

def solution(array):
    max_i = max(array)
    ans_list = [0]*max_i

    for x in array:
        ans_list[x] += 1
    
    ans_list.sort(reverse=True)
    if len(ans_list) > 1:
        if ans_list[0] == ans_list[1]:
            answer = -1
        else:
            answer = ans_list[0]
    else:
        answer=ans_list[0]

    return answer