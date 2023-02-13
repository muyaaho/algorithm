def solution(num, total):
    start = total//num - num//2
    start += 0 if num%2 != 0 else 1
    return list(range(start, start+num))