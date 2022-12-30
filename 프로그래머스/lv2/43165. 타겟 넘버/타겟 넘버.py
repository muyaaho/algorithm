def solution(numbers, target):
    answer = []
    
    def cal(arr, start):
        if not arr: 
            answer.append(start)
            return 
        
        cal(arr[1:], start+arr[0])
        cal(arr[1:], start-arr[0])
    
    cal(numbers[1:], +numbers[0])
    cal(numbers[1:], -numbers[0])
    
    return answer.count(target)