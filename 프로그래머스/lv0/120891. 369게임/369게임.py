from collections import Counter

def solution(order):
    return Counter(str(order))["3"] + Counter(str(order))["6"] + Counter(str(order))["9"]