def solution(numlist:list , n:int) -> int:
    return sorted(numlist, key=lambda x:(abs(n-x), -x))