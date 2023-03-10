#commit 메시지 수정
from collections import Counter

def solution(n, lost, reserve):
    # 배열 인덱스 접근, 인덱스 만들기 (보통 1벌, 없으면 0벌, 있으면 2벌)
    arr = [1]*(n+1)
    for x in sorted(lost):  
        arr[x] -= 1
    for x in sorted(reserve):
        arr[x] += 1
    
    for x in range(1, n+1):
        if arr[x] > 1:                      # 빌려줄 수 있는 사람이면
            if x-1>0 and arr[x-1] == 0:     # 앞사람한테 빌려주기
                arr[x-1] += 1
                arr[x] -=1
            elif x+1<n+1 and arr[x+1] == 0:  # 뒷사람한테 빌려주기
                arr[x+1] += 1
                arr[x] -= 1

    count = Counter(arr)
    try:
        answer = n-count[0]
    except:
        answer = n

    return answer
