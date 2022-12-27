def solution(nums):
    answer = 0
    divnum = len(nums)//2
    snums = set(nums)
    
    if divnum > len(snums):
        answer = len(snums)
    else:
        answer = divnum
    return answer