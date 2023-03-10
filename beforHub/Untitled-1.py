from collections import Counter

def solution(participant, completion):
    dict={}
    sumHash = 0

    for name in participant:
        dict[hash(name)] = name
        sumHash += hash(name)
    
    for name in completion:
        sumHash -= hash(name)

    answer = dict[sumHash]
    return answer