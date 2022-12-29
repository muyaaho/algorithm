def solution(array, n):
    array.sort()
    answer = sorted(array, key=lambda x: abs(n-x))
    print(answer)
    return answer[0]