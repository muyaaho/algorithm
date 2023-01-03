from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for start, to in sorted(edge):
        graph[start].append(to)
        graph[to].append(start)
    
    q = deque()
    q.append(1)
    v = [0]*(n+1)
    v[1] = 1
    
    while q:
        now = q.popleft()
        for to in graph[now]:
            if v[to] == 0:
                v[to] = v[now]+1
                q.append(to)
            
    return v.count(max(v))