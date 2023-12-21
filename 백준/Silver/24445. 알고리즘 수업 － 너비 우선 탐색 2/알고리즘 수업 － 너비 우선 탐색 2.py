from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    
    graph[u].append(v)
    graph[v].append(u)

for i in range(n+1):
    graph[i].sort(reverse=True)

visited = [0] * (n+1)
visited[r] = 1
q = deque()
q.append(r)

cnt = 2
while q:
    now = q.popleft()
    for next in graph[now]:
        if visited[next] == 0:
            visited[next] = cnt
            cnt += 1
            q.append(next)

print(*visited[1:], sep='\n')