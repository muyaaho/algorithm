def solution(N, stages):
    arr = []
    p = len(stages)
    for x in range(1, N+1):
        if p == 0:
            fail = 0
        else:
            fail = stages.count(x)/p
        arr.append((x, fail))
        p -= stages.count(x)
        
    arr = sorted(arr, key=lambda x:(-x[1], x[0]))
    answer = [i for i, j in arr]
    return answer