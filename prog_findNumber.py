def solution(num, k):
    
    arr = []
    answer = 0
    cnt = 0
    
    while num>0:
        arr.append(num%10)
        num //= 10
    
    print('arr: ',arr)
    for x in arr[::-1]:
        cnt += 1
        if x not in arr:
            answer = -1
            break
            
        elif x == k:
            answer = cnt
            break

    return answer

print(solution(232443, 4))