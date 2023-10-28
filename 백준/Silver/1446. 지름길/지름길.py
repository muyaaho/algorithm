import sys
input = sys.stdin.readline
from collections import deque

n, d = map(int, input().split())
graph = [[] for _ in range(d+1)]
distance = [int(1e9)] * (d+1)

for i in range(d):
    graph[i].append((i+1, 1))

for _ in range(n):
    start, end, cost = map(int, input().split())
    
    if end > d:
        continue
    graph[start].append((end, cost))
    
q = deque()
q.append((0, 0))
distance[0] = 0

while q:
    node, now_dist = q.popleft()
    for end, dist in graph[node]:
        cost = dist + distance[node]
        if cost < distance[end]:
            distance[end] = cost
            q.append((end, cost))
print(distance[-1])
