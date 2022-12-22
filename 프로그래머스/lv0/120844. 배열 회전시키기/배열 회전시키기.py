def solution(numbers, direction):
    answer = []
    if direction == "right":
        answer.append(numbers[-1])
        for x in numbers[:-1]:
            answer.append(x)
    else:
        for x in numbers[1:]:
            answer.append(x)
        answer.append(numbers[0])
    return answer