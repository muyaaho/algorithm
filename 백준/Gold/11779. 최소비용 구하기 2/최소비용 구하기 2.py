from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

q = []
parent = [0] * (n+1)
heappush(q, (0, start))
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
            parent[next] = now
            heappush(q, (c, next))

print(distance[end])

path = []
curr = end
while curr:
    path.append(curr)
    curr = parent[curr]

print(len(path))
print(*reversed(path), end=' ')
    