def solution(numbers):
    n = list(map(str, numbers))
    n = sorted(n, key=lambda x: x*3, reverse=True)
    return str(int(''.join(n)))