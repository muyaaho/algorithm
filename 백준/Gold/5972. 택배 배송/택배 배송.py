from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

q = []
heappush(q, (0, 1))
distance = [INF] * (n+1)
distance[1] = 0

while q:
    dist, now = heappop(q)
    
    if dist > distance[now]:
        continue
    
    for cost, next in graph[now]:
        c = cost + dist
        if c < distance[next]:
            distance[next] = c
            heappush(q, (c, next))

print(distance[n])