from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    
    for start, end in sorted(edge):
        graph[start].append(end)
        graph[end].append(start)
    
    q = deque()
    q.append(1)
    answer = [0]*(n+1)
    answer[1] = 1
    while q:
        now = q.popleft()
        for des in graph[now]:
            if answer[des] == 0:
                q.append(des)
                answer[des] = answer[now]+1
    return answer.count(max(answer))