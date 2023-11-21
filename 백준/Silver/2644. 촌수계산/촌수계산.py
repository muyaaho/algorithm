from collections import deque

n = int(input())
a, b = map(int, input().split())
graph = [[] for _ in range(n+1)]
m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    graph[y].append(x)
    graph[x].append(y)

q = deque([a])
distance = [-1] * (n+1)
distance[a] = 0

while q:
    now = q.popleft()
    if now == b:
        break
    for next in graph[now]:
        if distance[next] < 0:
            distance[next] = distance[now] + 1
            q.append(next)

print(distance[b])