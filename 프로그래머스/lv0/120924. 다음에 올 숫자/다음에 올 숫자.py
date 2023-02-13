def solution(common):
    a = common[1] - common[0]
    b = common[2] - common[1]
    if a == b:
        return common[-1] + a
    else:
        return common[-1] * (common[1] // common[0])