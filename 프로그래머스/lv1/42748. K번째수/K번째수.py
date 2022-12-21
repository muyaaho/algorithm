def solution(array, commands):
    answer = []
    for i, j, k in commands:
        # print(f'i: {i}, j:{j}, k:{k}')
        # print(sorted(array[i-1:j]))
        answer.append(sorted(array[i-1:j])[k-1])
    return answer