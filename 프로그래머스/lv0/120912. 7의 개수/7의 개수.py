def solution(array):
    arr = list(map(str, array))
    return sum([x.count('7') for x in arr])