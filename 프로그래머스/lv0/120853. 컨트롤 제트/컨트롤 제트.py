def solution(s):
    arr=[]
    for x in s.split():
        if x == 'Z':
            arr.pop()
        else:
            arr.append(int(x))
    
    return sum(arr)