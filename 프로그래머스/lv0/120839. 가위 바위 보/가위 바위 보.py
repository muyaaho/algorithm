def solution(rsp):
    dict = {"2":"0", "0":"5", "5":"2"}
    #print(list(rsp))
    answer = ''.join([dict[x] for x in list(rsp)])
    return answer