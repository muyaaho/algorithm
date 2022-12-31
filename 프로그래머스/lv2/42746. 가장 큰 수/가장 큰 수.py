def solution(numbers):
    n = [str(x) for x in numbers]
    n.sort(key=lambda x: x*3, reverse=True)
    return str(int("".join(n)))