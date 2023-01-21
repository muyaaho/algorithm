from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

q = deque()
q.append(x)
v = [-1]*(n+1)
v[x] = 0

while q:
    now = q.popleft()
    if v[now] == k:
        break
    for to in graph[now]:
        if v[to] == -1:
            v[to] = v[now] + 1
            q.append(to)

c = False
for i, x in enumerate(v):
    if x == k:
        c = True
        print(i)
    

if not c:
    print(-1)