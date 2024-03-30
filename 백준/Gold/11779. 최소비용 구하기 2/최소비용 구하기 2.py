from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

q = []
heappush(q, (0, start))
parent = [0] * (n+1)
distance = [int(1e9)] * (n+1)
distance[start] = 0

while q:
    dist, now = heappop(q)
    if dist > distance[now]:
        continue
    
    for next, cost in graph[now]:
        c = cost + dist
        if c < distance[next]:
            distance[next] = c
            heappush(q, (c, next))
            parent[next] = now

path = []
curr = end
while curr:
    path.append(curr)
    curr = parent[curr]
    
print(distance[end])
print(len(path))
print(*reversed(path), end=' ')