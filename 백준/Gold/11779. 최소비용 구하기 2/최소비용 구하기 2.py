from heapq import heappush, heappop
import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((cost, b))

start, end = map(int, input().split())

q = []
heappush(q, (0, start))
distance = [INF] * (n+1)
distance[start] = 0
parents = [0] * (n+1)

while q:
    dist, now = heappop(q)
    
    if dist > distance[now]:
        continue
    
    for cost, next in graph[now]:
        c = cost + dist
        if c < distance[next]:
            distance[next] = c
            parents[next] = now
            heappush(q, (c, next))

print(distance[end])

path = []  # 경로
curr = end
while curr:
    path.append(curr)
    curr = parents[curr]
print(len(path))
for i in path[::-1]:  # 경로 출력
    print(i, end=" ")
