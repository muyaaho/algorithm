import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [set() for _ in range(n+1)]
# print(graph)
for _ in range(m):
    to, end = map(int, input().split())
    graph[end].add(to)

# print(graph)
target = int(input())

q = deque()
visit = [False]*(n+1)
visit[target] = True
q.append(target)

ans = 0
while q:
    t = q.popleft()
    for x in graph[t]:
        if not visit[x]:
            visit[x] = True
            ans += 1
            q.append(x)

print(ans)