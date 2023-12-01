from heapq import heappush, heappop
import sys
input = sys.stdin.readline

INF = int(1e9)
n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

v1, v2 = map(int, input().split())

def dijkstra(start, end):
    q = []
    heappush(q, (0, start))
    distance = [INF] * (n+1)
    distance[start] = 0
    
    while q:
        dist, now = heappop(q)
        if dist > distance[now]:
            continue
        for cost, next in graph[now]:
            c = cost + dist
            if c < distance[next]:
                distance[next] = c
                heappush(q, (c, next))
    return distance[end]

path1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
path2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

answer = min(path1, path2)
print(-1 if answer >= INF else answer)