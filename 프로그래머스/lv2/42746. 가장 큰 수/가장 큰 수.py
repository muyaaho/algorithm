def solution(numbers):
    n = list(map(str, numbers))
    n.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(n)))