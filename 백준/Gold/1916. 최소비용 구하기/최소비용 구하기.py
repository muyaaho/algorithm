from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

wstart, wend = map(int, input().split())

q = []
# 그 점의 비용, 시작점
heappush(q,(0, wstart))
distance = [INF] * (n+1)
distance[wstart] = 0

while q:
    dist, now = heappop(q)
    if distance[now] < dist:
        continue
    for end, cost in graph[now]:
        c = cost + dist
        # print(cost)
        if c < distance[end]:
            distance[end] = c
            heappush(q, (c, end))

print(distance[wend])