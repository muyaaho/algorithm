import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

ans = {i:0 for i in range(n+1)}


for i in range(1, n+1):

    q = deque([i])
    visit = [False] * (n+1)
    visit[i] = True
    
    count = 0
    while q:
        node = q.popleft()
        for to in graph[node]:
            if not visit[to]:
                q.append(to)
                ans[i] += 1
                visit[to] = True


print(*[k for k, v in ans.items() if max(ans.values()) == v])