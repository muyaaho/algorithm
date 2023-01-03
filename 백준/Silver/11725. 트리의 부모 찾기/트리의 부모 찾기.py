from collections import deque

n = int(input())
edge = [list(map(int, input().split())) for _ in range(n-1)]
graph = [[] for _ in range(n+1)]
visit = [0]*(n+1)

for start, to in sorted(edge):
    graph[start].append(to)
    graph[to].append(start)

q = deque()
q.append(1)
visit[1] = 1

while q:
    now = q.popleft()
    for to in graph[now]:
        if visit[to] == 0:
            visit[to] = now
            q.append(to)

for x in visit[2:]:
    print(x)