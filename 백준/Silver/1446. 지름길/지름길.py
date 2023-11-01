from heapq import heappush, heappop
from collections import deque

n, d = map(int, input().split())
graph = [[] for _ in range(d+1)]

for i in range(d):
    graph[i].append((i+1, 1))

for _ in range(n):
    start, end, cost= map(int, input().split())
    if end > d:
        continue
    graph[start].append((end, cost))

q =[]
# 큐에 뭐가 들어가는지 기억하자 .. ㅠㅠ 그냥 0,0 썻단 것만 기억난다..
heappush(q, (0, 0))
distance = [int(1e9)] * (d+1)
distance[0] = 0

while q:
    start, dist = heappop(q)
    for end, cost in graph[start]:
        c = dist + cost
        if c < distance[end]:
            heappush(q, (end, c))
            distance[end] = c

print(distance[-1])
