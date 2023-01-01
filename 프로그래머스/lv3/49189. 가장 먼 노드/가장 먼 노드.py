from collections import deque

def solution(n, edge):
    answer = 0
    edge.sort()
    graph = [[] for x in range(n+1)]
    route = [0]*(n+1)
    
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)
    # print(graph)
    q = deque()
    q.append(1)
    route[1] = 1
    
    while q:
        now = q.popleft()
        for end in graph[now]:
            if route[end] == 0:
                q.append(end)
                route[end] = route[now]+1

    return route.count(max(route))