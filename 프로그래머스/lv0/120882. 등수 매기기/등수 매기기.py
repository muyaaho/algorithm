from collections import Counter

def solution(score):
    avg = [sum(a)/2 for a in score]
    dict = {num:rank for rank, num in enumerate(sorted(avg, reverse=True), start = 1)}
    c = Counter(avg)
    
    return [dict[a] - (c[a]-1) for a in avg]