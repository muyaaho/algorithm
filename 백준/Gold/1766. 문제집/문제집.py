from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = []
for i in range(1, n+1):
    if indegree[i] == 0:
        heappush(q, i)

while q:
    now = heappop(q)
    print(now, end=' ')
    for next in graph[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            heappush(q, next)