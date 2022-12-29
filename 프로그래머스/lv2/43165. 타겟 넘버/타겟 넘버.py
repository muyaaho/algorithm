from collections import Counter

def solution(numbers, target):
    answer = []
    
    def func(arr, x):
        # arr가 없으면 리스트에 값 append 하기
        if not arr:
            answer.append(x)
            return
        # 아니면 더하거나 빼서 함수 진행
        func(arr[1:], x+arr[0])
        func(arr[1:], x-arr[0])
    
    func(numbers, 0)
    return Counter(answer)[target]