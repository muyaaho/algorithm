def solution(citations):
    citations.sort(reverse=True)
    for i,x in enumerate(citations):
        if i >= x:
            return i
    return len(citations)