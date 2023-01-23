def solution(n):
    arr = ''
    while n:
        arr += str(n%3)
        n//=3
    return int(arr, 3)