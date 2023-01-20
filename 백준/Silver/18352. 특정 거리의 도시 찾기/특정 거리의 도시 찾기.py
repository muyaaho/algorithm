from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

q = deque()
v = [-1]*(n+1)
q.append(x)
v[x] = 0
while q:
    now = q.popleft()
    if v[now] == k:
        break
    for to_go in graph[now]:
        if v[to_go] == -1:
            v[to_go] = v[now]+1
            q.append(to_go)

if k in v:
    for i, x in enumerate(v):
        if x == k:
            print(i)
else:
    print(-1)