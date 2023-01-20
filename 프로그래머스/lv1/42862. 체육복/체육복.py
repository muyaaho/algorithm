def solution(n, lost, reserve):
    answer = 0
    k = 0
    # 중복데이터 제거 및 카운팅
    cp_lost = lost[:]
    cp_reserve =reserve[:]

    for i in range(len(lost)):
        if lost[i] in reserve:            
            cp_reserve.remove(lost[i])
            cp_lost.remove(lost[i])
    cp_lost.sort()
    cp_reserve.sort()
    while cp_lost and cp_reserve:
        v = cp_lost.pop(0)
        if v-1 in cp_reserve:
            cp_reserve.remove(v-1)
        elif v+1 in cp_reserve:
            cp_reserve.remove(v+1)
        else:
            k += 1

    if cp_lost:
        k = k + len(cp_lost)
    answer = n - k 
    return answer