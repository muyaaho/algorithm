def solution(s):
    l = s.split(' ')
    arr=[]
    
    for x in l:
        if x[0] == '-':
            arr.append(-int(x[1:]))
        else:
            arr.append(int(x))
    
    arr.sort()
    return str(arr[0])+' '+str(arr[-1])