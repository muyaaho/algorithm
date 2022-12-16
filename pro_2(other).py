a=[1,1,2,2]

def solution(array):
    while len(array) != 0:
        print('set(array)', set(array))
        #print('enumerate', enumerate(set(array)))
        #print('enumerate', enumerate(array))
        count = 0
        for i, a in enumerate(set(array)):
            print('\n',count,'번째 반복')
            count +=1
            print('i, a: ',i,a)
            array.remove(a)
            print('remove 뒤 array', array)
        
        print('\nfor 끝나고 array: ',array)
        if i==0: return a
    return -1

print(solution(a))