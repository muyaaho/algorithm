def solution(numbers, k):
    answer, b = 1, 3
    for x in range(k-1):
        answer = (answer+2)%len(numbers)
    return answer