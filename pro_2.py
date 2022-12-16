#최빈값 구하기

a=[0,0,0,0]

def solution(array):
    dict = {}
    
    for x in array:
        if x not in dict.keys():
            dict[x]=1
        else:
            dict[x] += 1
    #print('dict', dict)

    if len(dict.keys())>1 :
        d2 = sorted(dict.items(), key = lambda x:x[1], reverse=True)
        #print('d2: ',d2)
        if(d2[0][1] == d2[1][1]):
            answer = -1
        else:
            answer = d2[0][0]
    else:
        answer = next(iter(dict))
        #print('iter,', next(iter(dict)))


    return answer


print(solution(a))
