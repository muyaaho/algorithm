from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
visit = [0]*(n+1)

for x in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append(1)
visit[1] = 1

while q:
    now = q.popleft()
    for to in graph[now]:
        if visit[to] == 0:
            visit[to] = now
            q.append(to)

for x in visit[2:]:
    print(x)