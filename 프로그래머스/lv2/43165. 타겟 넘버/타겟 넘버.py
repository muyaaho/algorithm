def solution(numbers, target):
    answer = []
    
    def func(arr, start):
        if not arr:
            if start == target: answer.append(1)
            return
        func(arr[1:], start+arr[0])
        func(arr[1:], start-arr[0])
    
    func(numbers, 0)
    return len(answer)