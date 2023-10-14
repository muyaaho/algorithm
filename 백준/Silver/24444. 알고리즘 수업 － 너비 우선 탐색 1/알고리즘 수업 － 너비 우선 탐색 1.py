from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
visited = [0] * (n+1)
q.append(r)
visited[r] = 1

# 오름차순으로 방문하도록
for nodes in graph:
    nodes.sort()

cnt = 1
while q:
    now = q.popleft()
    for to_go in graph[now]:
        if visited[to_go] == 0:
            cnt += 1
            q.append(to_go)
            visited[to_go] = cnt
            
print(*visited[1:], sep='\n')